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
            if not re.search("(?:.*id|index)", str(column), re.IGNORECASE):
                self.replaceColumnsData(column)
                char = chr(ord(char) + 1)
        return self.df

    @abstractmethod
    def replaceColumnsData(self, column_name, tableHeader):
        pass

class ItemAnonymizer(Anonymizer):
    def __init__(self, df):
        super().__init__(df)

    def replaceColumnsData(self, column_name):
        words_anonymization = {}
        vectorizer  = CountVectorizer(token_pattern=r'(?u)\b\w+\b')
        analyze     = vectorizer.build_analyzer()
        cleaned_words = []

        self.df[column_name] = self.df[column_name].astype(str)
        for row_index, value in enumerate(self.df[column_name]):
            value = str(value)
            cleaned_words = analyze(value)
            for wordNum , word in enumerate(cleaned_words):
                if word not in words_anonymization:
                    words_anonymization[word] = column_name[0:2] + str(row_index) + str(wordNum)

                cleaned_words[wordNum] = words_anonymization[word]
            self.df.at[row_index, column_name] = " ".join(str(x) for x in cleaned_words)

        return self.df

df = pd.read_csv("./movies.csv")
anon = ItemAnonymizer(df)
data = anon.anonymize("items")
print(data.head(50).to_string())
data.to_csv('anon.csv')
