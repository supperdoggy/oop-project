using System;
namespace csclient
{
    public class User
    {
        public Int64 id;
        public String user_secret_key;
        public String username;
        public String password;
        public String tasks;
        public String date_created;

        public User(Int64 i, String sk, String u, String p, String t, String d)
        {
            id = i;
            user_secret_key = sk;
            username = u;
            password = p;
            tasks = t;
            date_created = d;
        }
    }
}
