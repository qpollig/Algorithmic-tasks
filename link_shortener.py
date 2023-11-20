from random import randint


class MarsURLEncoder:

    def __init__(self):
        self.lint_dict = {}

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        count = 0
        while count == 0:
            hash_url = randint(999, 9999) + randint(33, 12345)
            if hash_url not in self.lint_dict.keys():
                short_url = 'https://ma.rs/' + str(hash_url)
                self.lint_dict.update({short_url: long_url})
                count += 1
        return short_url

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        return self.lint_dict.get(short_url)
