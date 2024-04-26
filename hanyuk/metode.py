import requests,bs4,json,os,sys,random,datetime,time,re
from bs4 import BeautifulSoup as sop, BeautifulSoup
from rich.panel import Panel as nel, Panel
from rich import print as prints
from rich.tree import Tree
# // [ -------------- Instagram -------------- ]
# ink folower = https://z-p42.www.instagram.com/api/v1/friendships/{user_id}/followers/
# link mutual folower =  https://z-p42.www.instagram.com/api/v1/friendships/{user_id}/mutual_followers/
# link folowing = https://z-p42.www.instagram.com/api/v1/friendships/{user_id}/following/
# link media = https://z-p42.www.instagram.com/api/v1/feed/user/{user_id}/
# link feed favorite = https://z-p42.www.instagram.com/api/v1/friendships/update_feed_favorites/
# link ubah profile = https://z-p42.www.instagram.com/api/v1/web/accounts/web_change_profile_picture/
# link get profile pic props = https://z-p42.www.instagram.com/api/v1/web/get_profile_pic_props/{username}/
# link besties = https://z-p42.www.instagram.com/api/v1/friendships/set_besties/
# link komen = https://z-p42.www.instagram.com/api/v1/web/comments/{media_id}/delete/{comment_id}/
# link like = https://z-p42.www.instagram.com/api/v1/web/comments/like/{comment_id}/
# link unlike = https://z-p42.www.instagram.com/api/v1/web/comments/unlike/{comment_id}/
# link info user = https://z-p42.www.instagram.com/api/v1/users/{user_id}/info/
# link friendship show = https://z-p42.www.instagram.com/api/v1/friendships/show/{user_id}/