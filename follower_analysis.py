import requests
import pandas as pd

def get_followers(username, endpoint):
    """
    指定したユーザがフォローしているユーザのリストを取得する関数
    """
    followers = []
    page = 1
    per_page = 100  # 1ページあたりのユーザー数
    while True:
        url = f"https://api.github.com/users/{username}/{endpoint}?page={page}&per_page={per_page}"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            page_followers = [user["login"] for user in response.json()]
            followers.extend(page_followers)
            if len(page_followers) < per_page:
                break  # 最後のページまで取得した場合はループを終了
            page += 1
        elif response.status_code == 403 and "rate limit exceeded" in response.json()["message"]:
            print("API rate limit exceeded. Please try again later.")
            break
        else:
            print("Error:", response.status_code)
            break
    return followers

def main():
    my_username = input("Your GitHub username: ")
    
    # 自分がフォローしているユーザ
    my_following = get_followers(my_username, "following")
    # 自分をフォローしているユーザ
    my_followers = get_followers(my_username, "followers")
    
    if not my_following or not my_followers:
        return  # フォロワーリストが空の場合、処理を中断
    
    # 自分と相互にフォローしているユーザ
    mutual_followers = list(set(my_following) & set(my_followers))
    
    # 自分からフォローしているが、自分をフォローしていないユーザ
    following_not_followed_back = list(set(my_following) - set(my_followers))
    
    # 自分からフォローしていないが、自分をフォローしているユーザ
    followers_not_following = list(set(my_followers) - set(my_following))
    
    # 最大のリストの長さを取得
    max_length = max(len(mutual_followers), len(following_not_followed_back), len(followers_not_following))
    
    # データフレームを作成
    data = {
        "Mutual Followers": mutual_followers[:max_length],
        "Following Not Followed Back": following_not_followed_back[:max_length],
        "Followers Not Following Back": followers_not_following[:max_length]
    }
    df = pd.DataFrame(data)
    
    # 表形式で出力
    pd.set_option('display.max_rows', None)  # 行数の制限を解除
    print("\nData:")
    print(df.to_string(index=False))  # テーブル形式で表示

if __name__ == "__main__":
    main()
