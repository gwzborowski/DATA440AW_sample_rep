from src.data import make_data, save_data
from src.viz import make_figure

def main():
    data = make_data()
    save_data(data, 'test2.npy')
    make_figure(data, 'test_figure.svg')

    return None

if __name__ == "__main__":
    main()
