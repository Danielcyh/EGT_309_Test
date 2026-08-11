from class import ViltVQA

def main():
    vqa = ViltVQA()
    image = "faceimg.jpeg"
    questions = "What is the gender inside the image"
    answer = vqa.ask(image, questions)
    print(answer)

if __name__ == "__main__":
    main()

