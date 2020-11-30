def post_carousel(reply_token):
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {ENTER_ACCESS_TOKEN}"
    }
    payload = {
          "replyToken":reply_token,
          "messages":[
              {
                "type": "template",
                "altText": "おすすめレストラン",
                "template": {
                    "type": "carousel",
                    "columns": [

                        {
                          "thumbnailImageUrl": "https://s3-us-west-2.amazonaws.com/lineapitest/hamburger_240.jpeg",
                          "title": "ジャンク・バーガー",
                          "text": "誰が何と言おうとジャンクフードの王様は、今も昔も変わらずハンバーガー。",
                          "actions": [

                              {
                                  "type": "uri",
                                  "label": "詳細を見る",
                                  "uri": "http://example.com/page/222"
                              }
                          ]
                        },
                        {
                          "thumbnailImageUrl": "https://s3-us-west-2.amazonaws.com/lineapitest/pizza_240.jpeg",
                          "title": "pizza cap",
                          "text": "本場ナポリの味を早く、安く。都内に17店舗展開するピザ専門店です。",
                          "actions": [

                              {
                                  "type": "uri",
                                  "label": "詳細を見る",
                                  "uri": "http://example.com/page/222"
                              }
                          ]
                        },
                        {
                          "thumbnailImageUrl": "https://s3-us-west-2.amazonaws.com/lineapitest/bread_240.jpeg",
                          "title": "本格パン工房 たけよし",
                          "text": "パンにとって一番大事だと思うものはなんですか？たけよしは、表面の焼き上がりこそが命であると考えています。",
                          "actions": [

                              {
                                  "type": "uri",
                                  "label": "詳細を見る",
                                  "uri": "http://example.com/page/222"
                              }
                          ]
                        },
                        {
                          "thumbnailImageUrl": "https://s3-us-west-2.amazonaws.com/lineapitest/harumaki_240.jpeg",
                          "title": "ヴェトナムTokyo",
                          "text": "東池袋にあるしたベトナム料理の老舗。40年以上人々に愛され続けてきたベトナム料理をご提供します。",
                          "actions": [

                              {
                                  "type": "uri",
                                  "label": "詳細を見る",
                                  "uri": "http://example.com/page/222"
                              }
                          ]
                        },

                    ]
                }
              }
            ]
    }
    req = requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))