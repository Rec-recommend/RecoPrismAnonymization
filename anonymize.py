#!/usr/bin/python3
import re
import pandas as pd
from abc import abstractmethod, ABC
from sklearn.feature_extraction.text import CountVectorizer

class Anonymizer(ABC):
    def __init__(self, df):
        self.df = df

    def anonymize(self, tableName):
        tableHeader = tableName[0]
        self.df = self.renameColumnsHeader(tableHeader)
        return self.df

    def renameColumnsHeader(self, tableHeader):
        char = 'a'
        for column in self.df.columns:
            self.df.rename(columns={column: char}, inplace=True)
            self.replaceColumnsData(char, tableHeader)
            char = chr(ord(char) + 1)
        return self.df

    @abstractmethod
    def replaceColumnsData(self, column_name, tableHeader):
        pass




class UserAnonymizer(Anonymizer):
    def __init__(self, df):
        super().__init__(df)

    def replaceColumnsData(self, column_name, tableHeader):
        pattern = "^" + tableHeader + column_name + "[1-9]+$"
        for index, value in enumerate(self.df[column_name]):
            if not re.search(pattern, str(value)):
                self.df[column_name].replace({value: tableHeader + column_name + str(index)}, inplace=True)
        return self.df




class ItemAnonymizer(Anonymizer):
    def __init__(self, df):
        super().__init__(df)

    def replaceColumnsData(self, column_name ,tableHeader):
        self.df[column_name] = self.df[column_name].astype(str)
        words_anonymization = {}
        vectorizer  = CountVectorizer(token_pattern=r'(?u)\b\w+\b')
        analyze     = vectorizer.build_analyzer()
        cleaned_words = []

        for row_index, value in enumerate(self.df[column_name]):
            cleaned_words = analyze(value)
            for wordNum , word in enumerate(cleaned_words):
                if word not in words_anonymization:
                    words_anonymization[word] = tableHeader + column_name + str(row_index) + str(wordNum)

                cleaned_words[wordNum] = words_anonymization[word]
            self.df.at[row_index, column_name] = " ".join(str(x) for x in cleaned_words)

        return self.df

df = pd.read_csv("./movie_dataset_5000.csv")
anon = ItemAnonymizer(df)
data = anon.anonymize("users")
print(data.head(50).to_string())
data.to_csv('anon.csv')
