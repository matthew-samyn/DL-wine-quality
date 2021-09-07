import matplotlib.pyplot as plt
import itertools
import numpy as np


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()


def splitting_up_good_and_bad(quality):
    if quality <= 5:
        return 0
    else:
        return 1


def plot_and_print_loss(history):
    plt.plot(history.history['loss'], label='test_loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.ylim([0, 0.8])
    plt.xlabel('Epoch')
    plt.ylabel('Loss_score')
    plt.title("Comparing test to validation set")
    plt.legend()
    plt.grid(True)
    print(f"""Status at last epoch:
test_score = {history.history['loss'][-1]}
val_score  = {history.history['val_loss'][-1]}""")
    plt.show()
