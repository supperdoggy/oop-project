using System;
using System.Net;
using System.IO;
using System.Collections.Generic;
using System.Text;
using Newtonsoft.Json;

namespace csclient
{
    public class MainClass
    {
        
        public static void Main(string[] args)
        {

            string username;
            string password;

            Console.WriteLine("Enter your username: ");
            username = Console.ReadLine();
            Console.WriteLine("Enter your password: ");
            password = Console.ReadLine();

            string json = "{"+ $"\"username\":\"{username}\", \"password\":\"{password}\"" + "}";

            http.httpRequests request = new http.httpRequests("http://127.0.0.1:5000/login", json);
            var json1 = request.PostRequest();
            bool ok = json1["ok"];
            Console.Clear();

            if (ok == true)
            {
                User user = new User(json1["id"], json1["user_secret_key"], json1["username"], json1["password"], json1["tasks"], json1["date_created"]);
                Console.WriteLine($"Your id: {user.id}\nYour username: {user.username}\nYour password: {user.password}\nYour tasks: {user.tasks}\nYour date created: {user.date_created}");

            }
            else Console.WriteLine("Wrong password/username");
        }

    }

}
