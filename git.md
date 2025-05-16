git init

# cd to
(venv) eyob@eyob-ThinkPad:~/Desktop/gitpost/ebay1/ebay1scraper$ ls
ebay1scraper  scrapy.cfg
(venv) eyob@eyob-ThinkPad:~/Desktop/gitpost/ebay1/ebay1scraper$ echo "# eBay Product Scraper" > README.md
# code for adding readme
echo "# eBay Product Scraper" > README.md

# go to git hub and create repo and copy the link

https://github.com/ey0ba/ebay1.git

#  then in vscode go back to ebay1 dir termial and write
git init
git remote add origin https://github.com/ey0ba/ebay1.git

git remote -v
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main