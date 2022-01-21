from django.shortcuts import render
from allauth.socialaccount.providers.github.provider import GitHubAccount


def user_github(request):
    user_profile = GitHubAccount.get_profile_url()
    user_avatar = GitHubAccount.get_avatar_url
    context = {'user_profile': user_profile,
               'user_avatar': user_avatar}
    print('User profile is --->', user_profile)
    return render(request, 'base.html', context=context)

