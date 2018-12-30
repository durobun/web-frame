from django.http import HttpResponse

def get_list_by_user(request, username):
    print("username : ", username)
    return HttpResponse("{}의 블로그 글 리스트가 출력됩니다!".format(username))

def get_user_article(request, username, articleId):
    print("username : ", username)
    print("articleId", articleId)
    return HttpResponse("{}의 블로그 {}번 글이 출력됩니다!".format(username, articleId))