from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOpenAI()

# schema
class Review(TypedDict):

    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]
    

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The book was a thrilling read with a gripping plot and well-developed characters. The pacing was excellent, keeping me hooked from the beginning to the end.
                                 However, the ending felt a bit rushed and convenient writing, which was a letdown after such an engaging story. 
                                 Overall, I would recommend this book to anyone who enjoys a good thriller, but be prepared for a somewhat unsatu=isfying conclusion.
                                 Also, I liked the writer's complex writing style and the way they built the suspense throughout the book. The characters were well fleshed out, and
                                I found myself emotionally invested in their journeys. The plot twists were unexpected and kept me guessing until the very end.
                                 Despite the rushed ending, I still found the overall experience to be enjoyable and worth reading.
                                 But, I wish the author had taken more time to wrap up the story in a more satisfying way.
                                 And yes he has good scope for a sequel, which I would definitely look forward to reading.
                                 And also he can explore more on the characters in the next book, which I think has a lot of potential.
                                 Also he will someday become a popular writer, and I am excited to see what themes he might explore in the future.
Review by Shankar""")

print(result['name'])