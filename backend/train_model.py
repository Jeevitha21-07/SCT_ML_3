import os
import cv2
import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score
from skimage.feature import hog
import pickle

train_path = "dataset/training_set"
test_path = "dataset/test_set"

IMG_SIZE = 128

def extract_features(path):
    features = []
    labels = []

    for category in ["cats", "dogs"]:
        label = 0 if category == "cats" else 1
        folder = os.path.join(path, category)

        for img_name in os.listdir(folder):
            try:
                img_path = os.path.join(folder, img_name)
                img = cv2.imread(img_path)

                if img is None:
                    continue

                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                hog_features = hog(
                    gray,
                    orientations=9,
                    pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2),
                    block_norm='L2-Hys'
                )

                features.append(hog_features)
                labels.append(label)

            except:
                continue

    return np.array(features), np.array(labels)

print("Loading training data...")
X_train, y_train = extract_features(train_path)

print("Loading test data...")
X_test, y_test = extract_features(test_path)

print("Training SVM...")
model = svm.LinearSVC()
model.fit(X_train, y_train)

print("Evaluating...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("🔥 Accuracy:", accuracy)

pickle.dump(model, open("model.pkl", "wb"))
print("Model saved!")