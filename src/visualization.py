import matplotlib.pyplot as pt

def plot_word_frequency(df):
    top_words=df.head(10)

    pt.bar(top_words["Words"],top_words["Frequency"])

    pt.xlabel("Words")
    pt.ylabel("Frequency")
    pt.title("Most Common Words")

    pt.xticks(rotation=45)

    pt.tight_layout()

    pt.show()

    

