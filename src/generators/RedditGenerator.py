import praw

class RedditGenerator:
    def __init__(self, client_id: str, client_secret: str, subreddit: str) -> None:
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent="script_para_reddit"
        )
        self.subreddit = self.reddit.subreddit(subreddit)
        self.post = None  
        self.postTitle = None
        self.postDescription = None
        self.load_newest_post()  

    def load_newest_post(self):
        try:
            self.post = next(self.subreddit.new(limit=1))
            self.postTitle = self.post.title
            self.postDescription = self.post.selftext
        except StopIteration:
            print("Nenhum post disponível no subreddit.")
            self.post = None
            self.postTitle = "Sem título"
            self.postDescription = "Sem descrição"

    def get_post_title(self) -> str:
        return self.postTitle

    def get_post_description(self) -> str:
        return self.postDescription
