from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

emails = ["Win Instant Money", "Limited offer win cash", "Lottery Result", "Hello my friend", "Hope to meet you tomorrow"]

labels = ["spam", "spam", "spam", "not spam", "not spam"]

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(emails)

model = MultinomialNB()
model.fit(x, labels)

test_emails = ["Win Money Now"]
test_x = vectorizer.transform(test_emails)

prediction = model.predict(test_x)

print("Email: ", test_emails[0])
print("Prediction: ", prediction[0])