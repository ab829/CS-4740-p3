# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:19:37 2016

@author: ab829
"""

""""
for question in file, tokenize question, remove function words"
for folder pertaining to question, for file in folder:
    split into sentance
    tokenize sentance, remove function words
    if question words found,
    add original sentance to dictionary, value = # of question words found
    return top 5 answers from dictionary.
"""


"""
Returns a dictionary of questions and ids in the form of id:question
"""

def get_questions():
    questions = {}
    with open('question.txt', 'r') as f:
        q = f.xreadlines() #returns iterator
        for line in q:
            if line[:5] == "<num>":
                q_id = line[-3:]
                
        
    return questions
