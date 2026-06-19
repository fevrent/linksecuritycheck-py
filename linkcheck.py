print("Link Security Analyzer  ")

while True:
 link=input("Please enter the link you would like to test: ").strip()
 link_lower=link.lower()
 if link == "":
     print("Please enter a link ")
     
 if link_lower.startswith("https://"):
    print("Link is secure")
    break
 elif link_lower.startswith("http://"):
    print("link is not safe")
    break
 else:
    print("Link is invalid it must start with http:// or https://")
    print("Please try again")
