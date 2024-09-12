import requests
from datetime import datetime
import pyperclip
import sys
import tempfile
import os
import subprocess
from colorama import init, Fore, Style
from concurrent.futures import ThreadPoolExecutor, as_completed

# Initialize colorama
init(autoreset=True)

def check_usernames(username):
    platforms = {
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Paypal": f"https://www.paypal.com/paypalme/{username}",
        "GitHub": f"https://github.com/{username}",
        "Giters": f"https://giters.com/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Telegram": f"https://t.me/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Blogger": f"https://{username}.blogspot.com",
        "Tumblr": f"https://{username}.tumblr.com",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "About.me": f"https://about.me/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}",
        "Keybase": f"https://keybase.io/{username}",
        "Last.fm": f"https://www.last.fm/user/{username}",
        "Slideshare": f"https://www.slideshare.net/{username}",
        "Behance": f"https://www.behance.net/{username}",
        "Quora": f"https://www.quora.com/profile/{username}",
        "Patreon": f"https://www.patreon.com/{username}",
        "Myspace": f"https://myspace.com/{username}",
        "Kaggle": f"https://www.kaggle.com/{username}",
        "Periscope": f"https://www.pscp.tv/{username}",
        "Disqus": f"https://disqus.com/by/{username}",
        "Mastodon": f"https://mastodon.social/@{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Giphy": f"https://giphy.com/{username}",
        "LiveJournal": f"https://{username}.livejournal.com",
        "CodeWars": f"https://www.codewars.com/users/{username}",
        "Gumroad": f"https://gumroad.com/{username}",
        "Spotify": f"https://open.spotify.com/user/{username}",
        "Weebly": f"https://{username}.weebly.com",
        "YouTube": f"https://www.youtube.com/{username}",
        "ProductHunt": f"https://www.producthunt.com/@{username}",
        "Mix": f"https://mix.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "Strava": f"https://www.strava.com/athletes/{username}",
        "Internet Archive": f"https://archive.org/search?query={username}",
        "Twitter Archive": f"https://web.archive.org/web/*/https://twitter.com/{username}/status/*",
        "Linktree": f"https://linktr.ee/{username}",
        "Xbox": f"https://www.xboxgamertag.com/search/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Goodreads": f"https://www.goodreads.com/{username}",
        "VK": f"https://vk.com/{username}",
        "TripAdvisor": f"https://www.tripadvisor.com/members/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "AngelList": f"https://angel.co/{username}",
        "500px": f"https://500px.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "WhatsApp": f"https://wa.me/{username}",
        "Discord": f"https://discord.com/users/{username}",
        "Weibo": f"https://weibo.com/{username}",
        "OKCupid": f"https://www.okcupid.com/profile/{username}",
        "Meetup": f"https://www.meetup.com/members/{username}",
        "CodePen": f"https://codepen.io/{username}",
        "StackOverflow": f"https://stackoverflow.com/users/{username}",
        "HackerRank": f"https://www.hackerrank.com/{username}",
        "Xing": f"https://www.xing.com/profile/{username}",
        "Deezer": f"https://www.deezer.com/en/user/{username}",
        "Snapfish": f"https://www.snapfish.com/{username}",
        "Tidal": f"https://tidal.com/{username}",
        "Dailymotion": f"https://www.dailymotion.com/{username}",
        "Ravelry": f"https://www.ravelry.com/people/{username}",
        "ReverbNation": f"https://www.reverbnation.com/{username}",
        "Vine": f"https://vine.co/u/{username}",
        "Foursquare": f"https://foursquare.com/user/{username}",
        "Ello": f"https://ello.co/{username}",
        "Hootsuite": f"https://hootsuite.com/{username}",
        "Prezi": f"https://prezi.com/{username}",
        "Groupon": f"https://www.groupon.com/profile/{username}",
        "Joomla": f"https://www.joomla.org/user/{username}",
        "StackExchange": f"https://stackexchange.com/users/{username}",
        "Taringa": f"https://www.taringa.net/{username}",
        "Shopify": f"https://{username}.myshopify.com",
        "8tracks": f"https://8tracks.com/{username}",
        "Couchsurfing": f"https://www.couchsurfing.com/people/{username}",
        "OpenSea": f"https://opensea.io/{username}",
        "Trello": f"https://trello.com/{username}",
        "Fiverr": f"https://www.fiverr.com/{username}",
        "Badoo": f"https://badoo.com/profile/{username}",
        "Rumble": f"https://rumble.com/user/{username}",
        "Wix": f"https://www.wix.com/website/{username}",
    }

    results = [f"Searching for {username} on all social media platforms.\n"]

    def fetch_url(platform, url):
        try:
            response = requests.get(url, timeout=5)  # Added timeout for faster failure
            if response.status_code == 200:
                return f"[{datetime.now().strftime('%H:%M:%S')}] [+] | {platform}: {url}"
            else:
                return f"[{datetime.now().strftime('%H:%M:%S')}] [-] | {platform}: not found"
        except requests.RequestException as e:
            return f"[{datetime.now().strftime('%H:%M:%S')}] [-] | {platform}: error ({e})"

    # Use ThreadPoolExecutor to make concurrent requests
    with ThreadPoolExecutor(max_workers=20) as executor:  # Increased workers for faster execution
        future_to_platform = {executor.submit(fetch_url, platform, url): platform for platform, url in platforms.items()}

        for future in as_completed(future_to_platform):
            result = future.result()
            results.append(result)

            # Print each result in real-time
            sys.stdout.write(Fore.LIGHTBLACK_EX + result + '\n' + Style.RESET_ALL)
            sys.stdout.flush()

    results_text = "\n".join(results)

    return results_text  # Return results to be used in the menu

def main_menu():
    while True:
        username = input(Fore.LIGHTBLACK_EX + "Enter the username to search for: " + Style.RESET_ALL).strip()
        results_text = check_usernames(username)

        while True:
            print(Fore.LIGHTBLACK_EX + "\nChoose an option:")
            print("1. Copy results to clipboard")
            print("2. Save results to a temporary notepad")
            print("3. Go back to menu")
            print("4. Exit" + Style.RESET_ALL)

            choice = input(Fore.LIGHTBLACK_EX + "Enter your choice (1/2/3/4): " + Style.RESET_ALL).strip()

            if choice == '1':
                # Save to clipboard
                pyperclip.copy(results_text)
                print(Fore.LIGHTBLACK_EX + "Results have been copied to the clipboard." + Style.RESET_ALL)
                break
            elif choice == '2':
                # Save to a temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w', encoding='utf-8') as temp_file:
                    temp_file.write(results_text)
                    temp_file_path = temp_file.name

                print(Fore.LIGHTBLACK_EX + f"Results have been saved to a temporary notepad file: {temp_file_path}")
                print("The file will be deleted automatically when you close it." + Style.RESET_ALL)

                # Open the temporary file in the default text editor
                if os.name == 'nt':  # For Windows
                    os.startfile(temp_file_path)
                elif os.name == 'posix':  # For macOS and Linux
                    subprocess.call(['open' if sys.platform == 'darwin' else 'xdg-open', temp_file_path])

                break
            elif choice == '3':
                print(Fore.LIGHTBLACK_EX + "Returning to the menu..." + Style.RESET_ALL)
                break  # Break to go back to the main menu
            elif choice == '4':
                print(Fore.LIGHTBLACK_EX + "Exiting..." + Style.RESET_ALL)
                sys.exit()
            else:
                print(Fore.LIGHTBLACK_EX + "Invalid choice. Please enter 1, 2, 3, or 4." + Style.RESET_ALL)

if __name__ == "__main__":
    # ASCII Art Display
    ascii_art = """
  ██████  ███▄    █   ██████ 
▒██    ▒  ██ ▀█   █ ▒██    ▒ 
░ ▓██▄   ▓██  ▀█ ██▒░ ▓██▄   
  ▒   ██▒▓██▒  ▐▌██▒  ▒   ██▒
▒██████▒▒▒██░   ▓██░▒██████▒▒
▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░░ ░░   ░ ▒░░ ░▒  ░ ░
░  ░  ░     ░   ░ ░ ░  ░  ░  
      ░           ░       ░  
    """

    # Print ASCII art in gray
    print(Fore.LIGHTBLACK_EX + ascii_art + Style.RESET_ALL)

    main_menu()
