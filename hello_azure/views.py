from psycopg2 import connect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    print('Request for index page received')
    conn = connect(user="wsb", password="9a8346ec-545a-4e67-a9aa-3c8bedbd3511",
                   host="wsb-test-app-server.postgres.database.azure.com",
                   port=5432,
                   database="wsb")

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users;")
        x = cur.fetchall()
        user_name = x[0][0]
        user_surname = x[0][1]
    conn.close()

    return render(request, 'hello_azure/index.html', {"user_name": user_name, "user_surname": user_surname})


@csrf_exempt
def hello(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        if name is None or name == '':
            print("Request for hello page received with no name or blank name -- redirecting")
            return redirect('index')
        else:
            print("Request for hello page received with name=%s" % name)
            context = {'name': name}
            return render(request, 'hello_azure/hello.html', context)
    else:
        return redirect('index')


@csrf_exempt
def all_users(request):
    conn = connect(user="wsb", password="9a8346ec-545a-4e67-a9aa-3c8bedbd3511",
                   host="wsb-test-app-server.postgres.database.azure.com",
                   port=5432,
                   database="wsb")

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users;")
        u = cur.fetchall()
    conn.close()
    cur.close()
    context = {'users': u}
    print(context)

    return render(request, 'hello_azure/all.html', context)


@csrf_exempt
def add_user(request):
    return render(request, 'hello_azure/add_user.html')


@csrf_exempt
def add_user_post(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')

        conn = connect(user="wsb", password="9a8346ec-545a-4e67-a9aa-3c8bedbd3511",
                       host="wsb-test-app-server.postgres.database.azure.com",
                       port=5432,
                       database="wsb")

        with conn.cursor() as cur:
            sql = "INSERT INTO users (user_name, user_surname) VALUES (%s, %s);"
            data = (name, surname)

            cur.execute(sql, data)
            conn.commit()
            cur.close()
            conn.close()

        return redirect("https://wsb-test-app.azurewebsites.net/all")
    else:
        redirect("https://wsb-test-app.azurewebsites.net/all")


@csrf_exempt
def delete_user(request):
    return render(request, 'hello_azure/delete_user.html')


@csrf_exempt
def delete_user_post(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')

        conn = connect(user="wsb", password="9a8346ec-545a-4e67-a9aa-3c8bedbd3511",
                       host="wsb-test-app-server.postgres.database.azure.com",
                       port=5432,
                       database="wsb")

        with conn.cursor() as cur:
            sql = "DELETE FROM users WHERE user_name=%s AND user_surname=%s);"
            data = (name, surname)

            cur.execute(sql, data)
            conn.commit()
            cur.close()
            conn.close()

        return redirect("https://wsb-test-app.azurewebsites.net/all")
    else:
        redirect("https://wsb-test-app.azurewebsites.net/all")
