from instagrapi import Client
# import credentials
import time
import random
import colorama
from colorama import Fore
import validators
import maskpass



colorama.init(autoreset=True)
commen = ['Nice shot! ',
          'I love your profile! 😊 ',
          'Your feed is an inspiration 👍',
          'Just incredible 😮',
          'What camera did you use 📸 ',
          'Love your posts 🤗',
          'Looks awesome 👌',
          'Getting inspired by you 👏',
          '🙋‍ Yes!',
          'I can feel your passion 💪',
          'Awesome 👌',
          'Wow!😮']

print(Fore.LIGHTCYAN_EX + "*" * 25, Fore.LIGHTBLUE_EX + " INSTAGRAM - BOT ", Fore.LIGHTCYAN_EX + "*" * 25)
print(Fore.LIGHTCYAN_EX + "*" * 25, Fore.LIGHTBLUE_EX + "by:- Jayesh Jain", Fore.LIGHTCYAN_EX + "*" * 25)
print(Fore.LIGHTYELLOW_EX + "Establishing Secured Connection ")
client = Client()
colorama.init(autoreset=True)
time.sleep(random.randint(5, 10))
print(Fore.LIGHTGREEN_EX + "Succesfully Established !")
print(Fore.LIGHTRED_EX + "Warning :", Fore.RED + " Please Turn off your Two Factor Authentication Before Login ")
time.sleep(random.randint(1, 5))
a = (Fore.LIGHTMAGENTA_EX+f"Enter Instagram username : ")
username = input(a)

pa = (Fore.LIGHTMAGENTA_EX+f"Password: ")

pwd = maskpass.askpass(prompt=pa, mask="₹")
print(Fore.LIGHTYELLOW_EX + "Trying To Log-in")

try:

    client.login(username,pwd)
except Exception as e:
    e1 = str(e)
    a = e1.split(" ")
    for i in a:
        if i == 'password':
            print(Fore.LIGHTRED_EX + f"{e}\nThe password you entered is {pwd}")
            quit()
    print(Fore.LIGHTRED_EX+f"{e}")
    quit()

print(Fore.LIGHTGREEN_EX + "Succesfully logged in!! ^_^ ")
print(Fore.LIGHTRED_EX + "*" * 5, Fore.LIGHTRED_EX + "WARNING -",
      Fore.RED + " Please don't use The Bot Repeatedly Over a Short period of time ", Fore.LIGHTRED_EX + "*" * 5)
time.sleep(random.randint(2, 7))
print(Fore.LIGHTGREEN_EX + "please wait Loading Bot O_o")


def followBack(run):
    print(Fore.LIGHTYELLOW_EX + "FETCHING RECENT FOLLOWERS")
    user_id = client.user_id_from_username(username)
    followers = client.user_followers(user_id)
    following = client.user_following(user_id)
    diff = {k: v for k, v in followers.items() if k not in following}
    # print(diff)
    res = not bool(diff)
    if res == True:
        print(Fore.LIGHTRED_EX + "No Recent Followers found !")
        return 1
    keylist = list(diff.keys())
    already=[]
    try:
        with open(r'dont_delete_this_file.txt', 'r') as fp:
            for line in fp:
                # remove linebreak from a current name
                # linebreak is the last character of each line
                x = line[:-1]

                # add current item to the list
                already.append(x)
                exist=True

        if already:
            a = already[0]
            if a!=username:
                error

        else:
             error


    except:
        # print("Exception raised ")
        exist=False
        with open('dont_delete_this_file.txt', 'w') as fp:
            fp.write("%s\n" % username)
            for item in keylist:
                fp.write("%s\n" % item)
    print(Fore.LIGHTGREEN_EX + "Succesfully Fetched! ;)")
    if exist !=False:
        ch=input(Fore.LIGHTMAGENTA_EX+"Do  You want To send Request Again To Recent Followers Press n for No and anything else for yes! : ")
        if ch=="n":
            for key in diff.copy().keys():
                key = int(key)
                for i in already[1:]:
                    # print(i,":",key)
                    i = int(i)


                    if i == key:
                        # print("already followed")
                        x=str(key)
                        del diff[x]

            res = not bool(diff)
            if res == True:
                print(Fore.LIGHTRED_EX + "No Recent Followers found !")
                return 1
            newfollow=list(diff.keys())
            with open('dont_delete_this_file.txt', 'a') as fp:
                for item in newfollow:
                    fp.write("%s\n" % item)
        else:
            newfollow = list(diff.keys())
            with open('dont_delete_this_file.txt', 'w') as fp:
                fp.write("%s\n" % username)
                for item in newfollow:
                    fp.write("%s\n" % item)



    # with open('file.txt', 'w') as file:
    #     file.write(pickle.dumps(diff))
    # with open('finally.txt', 'w+',encoding="utf-8") as file:
    #     file.write(str(diff))

    print(Fore.LIGHTYELLOW_EX + "Trying To  follow Recent users !....")
    time.sleep(random.randint(2, 5))
    for i, media in enumerate(diff):
        # print(media)
        data = diff[media]
        # print(data)
        # print(type(data))

        if data.is_private == True:

            print(Fore.LIGHTYELLOW_EX + f"Trying to Follow (Private) user: {data.username} ")
        else:
            print(Fore.LIGHTYELLOW_EX + f"Trying to Follow (Public) user: {data.username} ")

        time.sleep(random.randint(5, 10))
        client.user_follow(data.pk)

        print(Fore.LIGHTGREEN_EX + f"Succesfully Followed user: {data.username} ")
    print(Fore.LIGHTGREEN_EX + "Succesfully Followed all recent followers ^_^")



def unFollow():
    try:
        ch = int(
            input(Fore.LIGHTMAGENTA_EX + "Enter 1 to unfollow all non-followers \nand 2 to unfollow all followers:  "))
    except:
        print(Fore.LIGHTRED_EX + "Sorry you have selected wrong input\nplease try again")
        return 1
    a = 1
    # print(diff)
    if ch == 2:
        print(Fore.LIGHTYELLOW_EX + "Please wait Fetching Followers!")
        followers = client.user_followers(client.user_id)

        res = not bool(followers)
        if res == True:
            print(Fore.LIGHTRED_EX + "No Followers found ")
            return 1

        print(Fore.LIGHTGREEN_EX + "Successfully Fetched!")
        # if res == True:
        #     print(Fore.LIGHTRED_EX+"No non followers found ")
        #     return 1
        for user_id in followers.keys():
            if a == 3:
                print(
                    Fore.LIGHTRED_EX + "Please Don't Unfollow more than 2 followers at same time \nPlease Try again Later !")
                return 1
            user = client.username_from_user_id(user_id)
            print(Fore.LIGHTYELLOW_EX + f"Unfollowing user : {user}")
            a += 1
            time.sleep(random.randint(1, 3))
            try:
                client.user_unfollow(user_id)
            except:
                continue
            print(Fore.LIGHTGREEN_EX + f"Successfully Unfollowed! {user}")

    elif ch == 1:
        print(Fore.LIGHTYELLOW_EX + "Please wait Fetching non Followers!")
        followers = client.user_followers(client.user_id)
        following = client.user_following(client.user_id)
        diff = {k: v for k, v in following.items() if k not in followers}
        res = not bool(diff)
        if res == True:
            print(Fore.LIGHTRED_EX + "No non followers found ")
            return 1

        for i, media in enumerate(diff):
            if a == 3:
                print(
                    Fore.LIGHTRED_EX + "Please Don't Unfollow more than 2 followers at same time \nPlease Try again Later !")
                return 1
            # print(media)
            data = diff[media]
            # print(data)
            # print(type(data))

            print(Fore.LIGHTYELLOW_EX + f"Trying to Unfollow user: {data.username} ")

            time.sleep(random.randint(2, 5))
            client.user_unfollow(data.pk)
            a += 1

            print(Fore.LIGHTGREEN_EX + f"Succesfully Unfollowed user: {data.username} ")
        print(Fore.LIGHTGREEN_EX + "Succesfully Unfollowed all non followers ^_^")
    else:
        print(Fore.LIGHTRED_EX + "Sorry you have selected wrong input\nplease try again")
        return 1


def searchLocation():
    lo1 = input(Fore.LIGHTMAGENTA_EX + "please enter the longitude and latitude to like post near that in (,) sep: ")
    try:
        lo, la = lo1.split(",")
    except:
        print(Fore.LIGHTRED_EX + "Sorry you have selected wrong input\nplease try again")
        return True

    print(Fore.LIGHTYELLOW_EX + "Fetching Location!")
    try:
        location = client.location_search(lo, la)[0]
        location1 = client.location_complete(location)
        a = location1.dict()
    except:
        print(Fore.LIGHTRED_EX + "No location found for this cordintes \nplease try again with new cordinates ")
        return 1
    # print(a)
    print(Fore.LIGHTGREEN_EX + f"Successfully Fetched! Location: {a['name']}")
    c = int(input(Fore.LIGHTMAGENTA_EX + f"ammount of post you want to fetch for {a['name']} : "))
    if c > 20:
        print(Fore.LIGHTRED_EX + "sorry! maximum 20  is Allowed")
        c = 20
    if c <= 0:
        print(Fore.LIGHTRED_EX + "Minimum 1 is allowed ")
        c = 1

    print(Fore.LIGHTYELLOW_EX + f"Fetching Top Posts in location : {a['name']}")

    medias = client.location_medias_top(a['pk'], amount=c)
    res = not bool(medias)
    if res == True:
        print(Fore.LIGHTRED_EX + f"Unfortunately no post found for {a['name']}")
        return True
    print(Fore.LIGHTGREEN_EX + "Successfully Fetched")
    cc = input(
        Fore.LIGHTMAGENTA_EX + "Do you want to Comment on posts? it can help you increase reach! Press y for yes: ")
    # print(medias)
    comen=random.randint(2,6)
    for i, media in enumerate(medias):
        u = media.user.username
        if i % comen == 0:
            if cc == "y":
                if media.has_liked == True:
                    continue
                r = random.choice(commen)
                r1 = r + " @" + u
                try:
                    client.media_comment(media.id, r1)
                except:
                    continue
                print(Fore.LIGHTCYAN_EX + f"Commented {r} under loc: {a['name']} Posted By {u}")
        try:
            client.media_like(media.id)
        except:
            time.sleep(random.randint(1, 5))
            continue

        print(Fore.LIGHTGREEN_EX + f"Liked post number {i + 1} of location: {a['name']} Posted By {u}")
        time.sleep(random.randint(1, 5))

    return 1


def hashTag():
    h = input(Fore.LIGHTMAGENTA_EX + "Please enter your Hashtag sep by (#) : ")
    hashtag1 = h.split("#")
    hashtag = hashtag1[1:]
    # print(hashtag)
    a = int(input(Fore.LIGHTMAGENTA_EX + "Please enter the number of post that you want to fetch for  each # : "))
    if a > 20:
        print(Fore.LIGHTRED_EX + "Sorry! max 20 is allowed ")
        a = 20
    if a <= 0:
        print(Fore.LIGHTRED_EX + "Minimum 1 is allowed ")
        a = 1
    cc = input((Fore.LIGHTMAGENTA_EX + "Do you want to Comment on posts? it can help you increase reach! Press y for yes: and n for no: "))
    comen = random.randint(2, 6)
    for has in hashtag:
        print(Fore.LIGHTYELLOW_EX + f"please Wait Fetching  Posts For #{has}")
        medias = client.hashtag_medias_recent(has.lower(), a)
        res = not bool(medias)
        if res == True:
            print(Fore.LIGHTRED_EX + f"Unfortunately no post found for #{has}")
            continue
        print(Fore.LIGHTGREEN_EX + f"Successfully Fetched Posts for #{has}")
        # medias.append(m)
        for i, media in enumerate(medias):
            u = media.user.username
            # print(media)
            if i % comen == 0:
                if cc == "y":
                    if media.has_liked==True:
                        continue
                    r = random.choice(commen)
                    r1 = r + " @" + u
                    try:
                        client.media_comment(media.id, r1)
                    except:
                        continue
                    print(Fore.LIGHTCYAN_EX + f"Commented {r} under #{has} Posted By {u}")
            try:
                client.media_like(media.id)
            except:
                time.sleep(random.randint(1, 5))
                continue
            print(Fore.LIGHTGREEN_EX + f"Liked post number {i + 1}  under #{has} Posted By {u}")
            time.sleep(random.randint(1, 5))



def sendMessage():
    try:
        ch = int(input(
            Fore.LIGHTMAGENTA_EX + "Enter 1 to send message to all following \nand 2 to send message all followers:  "))
    except:
        print(Fore.LIGHTRED_EX + "Sorry you have selected wrong input\nplease try again")
        return 1

    m = input(Fore.LIGHTMAGENTA_EX + "Please Enter the message that you want to send : ")

    ab=1
    # print(diff)
    if ch == 2:
        print(Fore.LIGHTYELLOW_EX + "Please wait Fetching Followers!")
        followers = client.user_followers(client.user_id)
        res = not bool(followers)
        if res == True:
            print(Fore.LIGHTRED_EX + "No Followers found ")
            return True
        for user_id in followers.keys():
            if ab%5==0:
                cho=input("Do You want to continue sending Messages press y for Yes")
                if cho!="y"or cho!="Y":
                    return 1
            user = client.username_from_user_id(user_id)
            print(Fore.LIGHTYELLOW_EX + f"Messaging user : {user}")
            time.sleep(random.randint(1, 3))
            try:
                client.direct_send(text=m, user_ids=[user_id])
            except:
                continue
            print(Fore.LIGHTGREEN_EX + f"Succesfully messaged user: {user} ")
            ab+=1

        print(Fore.LIGHTGREEN_EX + "Successfully Message send to all followers!")
        return 1

    elif ch == 1:
        following = client.user_following(client.user_id)

        res = not bool(following)

        if res == True:
            print(Fore.LIGHTRED_EX + "No following found ")
            return 1
        ab=1
        for user_id in following.keys():
            if ab%5==0:
                cho=input("Do You want to continue sending Messages press y for Yes")
                if cho!="y"or cho!="Y":
                    return 1
            user = client.username_from_user_id(user_id)
            print(Fore.LIGHTYELLOW_EX + f"Messaging user : {user}")
            time.sleep(random.randint(1, 3))
            try:
                client.direct_send(text=m, user_ids=[user_id])
            except:
                continue

            print(Fore.LIGHTGREEN_EX + f"Succesfully messaged user: {user} ")
            ab+=1
        print(Fore.LIGHTGREEN_EX + "Succesfully messaged all following ^_^")
        return 1

def copy():
    a=input(Fore.LIGHTMAGENTA_EX+"Please Enter the Username or the link of the profile Whose Followers/Following You want  to copy : ")
    valid = validators.url(a)
    print(Fore.LIGHTYELLOW_EX+"Please Wait Fetching Data From Link/Username")
    if valid == True:
        try:
            link1 = a.split("?")
            # print(link1)
            a = link1[0]
        except:
            pass
        link = a.split("m/")[1]
        if link[-1] == "/":
            username = link[:-1]

    else:
        if a[0] == "@":
            username = a[1:]
    try:
        user_id=client.user_id_from_username(username)
        print(Fore.LIGHTGREEN_EX+f"Account  Successfully Found For username :@{username}")
    except:
        print(Fore.LIGHTRED_EX+"Unfortunately No account Found For Username : ",username)
        return
    try:
        a = int(input(Fore.LIGHTMAGENTA_EX+"For Copying Followers Press 1 \n For Following press 2 : "))
    except:
        print(Fore.LIGHTRED_EX + "Sorry you have selected wrong input\nplease try again")
        return True
    if a<=0 or a>=3 :
        print(Fore.LIGHTRED_EX + "Sorry you have selected wrong input\nplease try again")
        return True
    if a==1:
        print(Fore.LIGHTYELLOW_EX + f"Please Wait Fetching Followers of @{username}")
        list11=client.user_followers(user_id)
        time.sleep(random.randint(1,3))
    if a==2:
        print(Fore.LIGHTYELLOW_EX + f"Please Wait Fetching Followings of @{username}")
        list11=client.user_following(user_id)
        time.sleep(random.randint(1,3))
    runned=0

    already=[]
    keylist=list(list11.keys())
    try:
        with open(r'dont_delete_this_file.txt', 'r') as fp:
            for line in fp:
                # remove linebreak from a current name
                # linebreak is the last character of each line
                x = line[:-1]

                # add current item to the list
                already.append(x)
                exist=True

        if already:
            a = already[0]
            if a!=username:
                error

        else:
             error


    except:
        # print("Exception raised ")
        exist=False
        with open('dont_delete_this_file.txt', 'w') as fp:
            fp.write("%s\n" % username)
            for item in keylist:
                fp.write("%s\n" % item)

    if exist !=False:
        # ch=input(Fore.LIGHTMAGENTA_EX+"Do  You want To send Request Again To Recent Followers Press n for No and anything else for yes! : ")
        # if ch=="n":
            for key in list11.copy().keys():
                key = int(key)
                for i in already[1:]:
                    # print(i,":",key)
                    i = int(i)


                    if i == key:
                        # print("already followed")
                        x=str(key)
                        del list11[x]

            res = not bool(list11)
            if res == True:
                print(Fore.LIGHTRED_EX + "No New Followers/Following  found To Follow !")
                return 1
            newfollow=list(list11.keys())
            with open('dont_delete_this_file.txt', 'a') as fp:
                for item in newfollow:
                    fp.write("%s\n" % item)


    print(Fore.LIGHTGREEN_EX+"SuccessFully Fetched !")

    for i, media in enumerate(list11):
        # print(media)
        data = list11[media]
        # print(data)
        # print(type(data))
        if runned==10:
            print(
                Fore.LIGHTRED_EX + "Please Don't follow more than 10 followers at same time \nPlease Try again Later !")
            return 1


        if data.is_private == True:

            print(Fore.LIGHTYELLOW_EX + f"Trying to Follow (Private) user: {data.username} ")
        else:
            print(Fore.LIGHTYELLOW_EX + f"Trying to Follow (Public) user: {data.username} ")

        time.sleep(random.randint(5, 10))
        client.user_follow(data.pk)
        runned+=1
        print(Fore.LIGHTGREEN_EX + f"Succesfully Followed user: {data.username} ")

def like():
    try:
        print(Fore.LIGHTMAGENTA_EX+"Enter 1 To like Posts Of  all Messengers \n Enter 2 To like Post of all Followers \n Enter 3 to like post of all Following")
        ch=int(input(Fore.LIGHTWHITE_EX+"Please Enter Here : "))
    except:
        print(Fore.LIGHTRED_EX+"Wrong input \n Please Try again Later..")
        return
    if ch<=0 or ch>3:
        print(Fore.LIGHTRED_EX + "Wrong input \n Please Try again Later..")
        return
    liked=1
    if ch==1:
        print(Fore.LIGHTYELLOW_EX+"Please Wait Fetching Users ")
        di1=client.direct_pending_inbox()
        di2 = client.direct_threads()
        di=di1+di2
        # print("di=",di)
        dm=[]
        print(Fore.LIGHTGREEN_EX+"Successfully Fetched !")

        for i,user in enumerate(di):
            a=user.messages
            for i,b in enumerate(a):
                if i==1:
                   break
                dm.append(b.user_id)
        for user_code in dm:

            name=client.username_from_user_id(user_code)
            try:
                medias=client.user_medias(user_code)
            except:
                print(Fore.LIGHTRED_EX+f"@{name}  is having Private account Moving To next one!")
                continue
            # print(medias)
            for i, media in enumerate(medias):
                # u = media.user.username
                if i==5:
                    print(Fore.LIGHTGREEN_EX+f"SuccessFully Liked ",Fore.LIGHTRED_EX+" 5 post ",Fore.LIGHTGREEN_EX+f"of @{name} Moving To another Now ")
                    break
                try:
                    client.media_like(media.id)
                except:
                    continue
                print(Fore.LIGHTGREEN_EX+f"Successfully Liked Post {i+1} of @{name}")
                time.sleep(random.randint(1,5))

            # print(Fore.LIGHTGREEN_EX+f"Successfully Liked all Posts of @{name}")

    if ch==2:
        print(Fore.LIGHTYELLOW_EX+"Please Wait Feching Followers !")
        diff=client.user_followers(client.user_id)
    if ch==3:
        print(Fore.LIGHTYELLOW_EX+"Please Wait Feching Following !")
        diff=client.user_following(client.user_id)
    for i, media in enumerate(diff):
        # print(media)
        data = diff[media]
        name=data.username
        user_code=client.user_id_from_username(name)

        try:

            medias=client.user_medias(user_code)
        except:
            print(Fore.LIGHTRED_EX+f"@{name}  is having Private account Moving To next one!")
            continue
        # print(medias)
        for i, media in enumerate(medias):
            # u = media.user.username
            # print(media)
            if i==5:
                print(Fore.LIGHTGREEN_EX + f"SuccessFully Liked ", Fore.LIGHTRED_EX + " 5 post ",
                      Fore.LIGHTGREEN_EX + f"of @{name} Moving To another Now ")
                break
            try:
                client.media_like(media.id)
            except:
                continue
            print(Fore.LIGHTGREEN_EX+f"Successfully Liked Post {i+1} of @{name}")
            time.sleep(random.randint(1,5))

        # print(Fore.LIGHTGREEN_EX+f"Successfully Liked all Posts of @{name}")








    # client.user_medias()
def main():
    run = 1
    i = 'y'

    while i != "n":
        print(Fore.LIGHTCYAN_EX + "_" * 50)
        print(Fore.LIGHTGREEN_EX + "\t\t\t\t\tMENU")
        print(Fore.LIGHTMAGENTA_EX + "Enter", Fore.LIGHTGREEN_EX + " 1",
              Fore.LIGHTMAGENTA_EX + " to follow Recent Followers")
        print(Fore.LIGHTMAGENTA_EX + "Enter", Fore.LIGHTGREEN_EX + " 2",
              Fore.LIGHTMAGENTA_EX + " to Like And Comment According To Location")
        print(Fore.LIGHTMAGENTA_EX + "Enter", Fore.LIGHTGREEN_EX + " 3", Fore.LIGHTMAGENTA_EX + " for hashtags")
        print(Fore.LIGHTMAGENTA_EX + "Enter", Fore.LIGHTGREEN_EX + " 4 ", Fore.LIGHTMAGENTA_EX + "for message")
        print(Fore.LIGHTMAGENTA_EX + "Enter ", Fore.LIGHTGREEN_EX + "5", Fore.LIGHTMAGENTA_EX + " to unfollow  ")
        print(Fore.LIGHTMAGENTA_EX + "Enter ", Fore.LIGHTGREEN_EX + "6", Fore.LIGHTMAGENTA_EX + " to copy Someone Follower/Following  ")
        print(Fore.LIGHTMAGENTA_EX + "Enter ", Fore.LIGHTGREEN_EX + "7", Fore.LIGHTMAGENTA_EX + " to Like User Posts ")
        print(Fore.LIGHTMAGENTA_EX + "Enter ", Fore.LIGHTRED_EX + "8", Fore.LIGHTMAGENTA_EX + " to End the Program")
        try:
            i = int(input(Fore.LIGHTWHITE_EX + "Please enter Your choice : "))
        except:
            print(Fore.LIGHTRED_EX+"Wrong input ! Please try Again ....")
            continue
        if i == 1:
            followBack(run)
            run += 1
            continue
        if i == 5:
            c = input(Fore.LIGHTMAGENTA_EX + "are you sure you want to unfollow (press y to continue) : ")
            if c == "y":
                a = unFollow()
            continue

        if i == 2:
            loc = searchLocation()
            continue
        if i == 4:
            sm = sendMessage()
            continue
        if i == 3:
            hashTag()
            continue
        if i==6:
            copy()
            continue
        if i==7:
            like()
            continue
        elif i==8:
            print(Fore.LIGHTCYAN_EX + "Thanks For using This Bot !!")
            break

    print(Fore.LIGHTYELLOW_EX + "please wait Logging  Out! ")
    time.sleep(random.randint(2, 7))
    client.logout()
    print(Fore.LIGHTGREEN_EX + "Successfully Logged out !")


if __name__ == '__main__':
    main()

