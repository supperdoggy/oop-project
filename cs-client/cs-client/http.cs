using System;
using System.Net;
using System.IO;
using System.Collections.Generic;
using System.Text;
using Newtonsoft.Json;

namespace csclient
{
    public class http
    {
        public class httpRequests
        {
            string url;
            string jsonData;

            public httpRequests(string u, string j)
            {
                url = u;
                jsonData = j;
            }

            public Dictionary<string, dynamic> PostRequest()
            {
                var httpWebRequest = (HttpWebRequest)WebRequest.Create($"{url}");
                httpWebRequest.ContentType = "application/json";
                httpWebRequest.Method = "POST";

                using (var streamWriter = new StreamWriter(httpWebRequest.GetRequestStream()))
                {
                    string json = jsonData;

                    streamWriter.Write(json);
                }

                HttpWebResponse httpResponse = (HttpWebResponse)httpWebRequest.GetResponse();
                using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
                {
                    var result = streamReader.ReadToEnd();

                    return JsonConvert.DeserializeObject<Dictionary<string, dynamic>>(result.ToString());

                }
            }

            public string getRequest()
            {
                WebRequest request = WebRequest.Create(
                  $"{url}");
                WebResponse response = request.GetResponse();
                using (Stream dataStream = response.GetResponseStream())
                {
                    // Open the stream using a StreamReader for easy access.  
                    StreamReader reader = new StreamReader(dataStream);
                    // Read the content.  
                    string responseFromServer = reader.ReadToEnd();
                    // Display the content.
                    return responseFromServer;
                }
            }
        }
    }
}
