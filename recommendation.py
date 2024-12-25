def recommend_content(emotion):
    content = {
        "happy": {
            "songs": [
                {"title": "Happy", "url": "https://music.youtube.com/watch?v=dJqxQzxLbHM&si=HjU4VZ_LNLyjZ6K4"},
                {"title": "Ilahi", "url": "https://music.youtube.com/watch?v=lSPNH_rYKIg&si=YamZ-woPJR7CrzZx"},
                {"title": "Phir Se Ud Chala",
                 "url": "https://music.youtube.com/watch?v=mb7-qmKLoe0&si=68oU99adJSVptBAz"},
                {"title": "On Top of the World",
                 "url": "https://music.youtube.com/watch?v=dj86haGuI8w&si=ao9TIBBc04BDGzgD"},
                {"title": "Aaj Kal Zindagi",
                 "url": "https://music.youtube.com/watch?v=Gh2yHcm4tQg&si=Bo-vgsZzKJHdoiEr"},
                {"title": "Ude Dil Befikre", "url": "https://music.youtube.com/watch?v=Sxu8wHE97Rk&si=S8qUftKebwmmO5D4"}
            ],
            "books": [
                {
                    "title": "The Happiness Project",
                    "url": "https://www.amazon.in/Happiness-Project-Tenth-Anniversary-Aristotle/dp/0062888749",
                    "description": "A memoir by Gretchen Rubin, exploring one woman's year-long quest to bring more happiness into her life and the lessons she learns along the way."
                },
                {
                    "title": "The Power of Now",
                    "url": "https://www.amazon.in/Power-Now-Practice-Attain-Enlightenment/dp/1393602568",
                    "description": "Eckhart Tolle's spiritual guide to living fully in the present moment, breaking free from the trappings of the mind and achieving inner peace."
                }
            ],
            "movies": [
                {
                    "title": "Zindagi Na Milegi Dobara (2011)",
                    "url": "https://www.youtube.com/watch?v=hfOZxqwHjzk",
                    "description": "A feel-good movie about friendship, adventure, and self-discovery set against a beautiful road trip through Spain."
                },
                {
                    "title": "Dil Dhadakne Do (2015)",
                    "url": "https://www.dailymotion.com/video/x3n5llc",
                    "description": "A light-hearted family drama set on a cruise, filled with humor, relationships, and picturesque locations."
                },
                {
                    "title": "Queen (2013)",
                    "url": "https://www.youtube.com/watch?v=Sd76mVUBPF4",
                    "description": "A delightful story of a woman who embarks on a solo honeymoon, discovering her independence and inner strength along the way."
                },
                {
                    "title": "3 Idiots (2009)",
                    "url": "https://www.youtube.com/watch?v=is4ZkFNLnnk",
                    "description": "A heartwarming comedy about friendship, chasing dreams, and questioning the norms of society, packed with laughs and emotional moments."
                },
                {
                    "title": "Dum Laga Ke Haisha (2015)",
                    "url": "https://www.youtube.com/watch?v=Y1AcrbkJpjk",
                    "description": "A charming, simple love story with relatable characters and light-hearted humor."
                }
            ],
            "yoga": [
                {
                    "title": "Surya Namaskar",
                    "url": "https://www.mondaycampaigns.org/wp-content/uploads/2020/03/destress-monday-yoga-infographic-sun-salutation.png",
                    "description": "A series of 12 yoga poses that flow into each other, promoting flexibility and strength while energizing the body."
                },
                {
                    "title": "Child Pose",
                    "url": "https://www.verywellfit.com/thmb/L1qqAtlF2_92QCCcmvKwHeAYpIo=/2500x1667/filters:fill(FFDB5D,1)/ChildsPose-5c5d94ce46e0fb00017dd0d9.jpg",
                    "description": "A resting pose that stretches the back and helps calm the mind, providing a sense of peace."
                },
                {
                    "title": "Warrior Pose",
                    "url": "https://srisrischoolofyoga.org/na/wp-content/uploads/2023/01/warrior-pose-three-variations-1-2-3.jpg",
                    "description": "A powerful pose that strengthens the legs and core while improving balance and concentration."
                }
            ]
        },
        "sad": {
            "songs": [
                {"title": "Phir Se Udd Chala",
                 "url": "https://music.youtube.com/watch?v=mb7-qmKLoe0&si=68oU99adJSVptBAz"},
                {"title": "Fix You", "url": "https://music.youtube.com/watch?v=Oncu0bgdcXU&si=VUuL50KfSoMYEmwF"},
                {"title": "Let It Be", "url": "https://music.youtube.com/watch?v=HzvDofigTKQ&si=0inGSi_qi3LJ5_z5"},
                {"title": "Aashayein", "url": "https://music.youtube.com/watch?v=hT5-kDr2vL4&si=5wpdufF4sOy4yWBU"},
                {"title": "Subhanallah", "url": "https://music.youtube.com/watch?v=pnJriqNxpcc&si=kSXXQCSST0xHRAyV"},
                {"title": "Dil Dhoondta Hai",
                 "url": "https://music.youtube.com/watch?v=tD8e3zvGMKg&si=yH5QWjEZrYNSCJlK"}
            ],
            "books": [
                {
                    "title": "The Fault in Our Stars",
                    "url": "https://www.amazon.in/Fault-our-Stars-John-Green/dp/0141345659",
                    "description": "A touching novel by John Green about two teenagers who fall in love while battling cancer, a story that explores love, loss, and the fragility of life."
                },
                {
                    "title": "All the Bright Places",
                    "url": "https://www.amazon.in/All-Bright-Places-Jennifer-Niven/dp/0141357037",
                    "description": "Jennifer Niven's young adult novel that delves into the story of two teenagers who form a deep bond as they help each other heal from their emotional struggles."
                }
            ],
            "movies": [
                {
                    "title": "Jab We Met (2007)",
                    "url": "https://www.youtube.com/watch?v=jf2gOSORoqU",
                    "description": "Jab We Met is a heartwarming romantic drama about two strangers who find love and personal growth through an unexpected journey together."
                },
                {
                    "title": "Tamasha (2015)",
                    "url": "https://www.dailymotion.com/video/x3i0wgd",
                    "description": "A beautifully crafted story about self-realization, breaking free from societal norms, and embracing one's true identity, with soulful music."
                },
                {
                    "title": "Taare Zameen Par (2007)",
                    "url": "https://www.youtube.com/watch?v=GMyN_tY1MIM",
                    "description": "An emotional yet inspiring film about a young boy with dyslexia, and how a compassionate teacher changes his life. It’s both touching and uplifting."
                },
                {
                    "title": "Kal Ho Naa Ho (2003)",
                    "url": "https://www.youtube.com/watch?v=c4tKB0kfhtw",
                    "description": "A bittersweet story about love, family, and living life to the fullest, with an emotional depth that leaves you both teary-eyed and hopeful."
                },
                {
                    "title": "Wake Up Sid (2009)",
                    "url": "https://www.youtube.com/watch?v=Uv8qyr5vc-o",
                    "description": "A coming-of-age film about a young man discovering responsibility and love, with gentle humor and emotional growth that can bring a smile."
                }
            ],
            "yoga": [
                {
                    "title": "Legs-Up-The-Wall",
                    "url": "https://th.bing.com/th/id/R.ae2a7b5016d30825c59420ea587a5eb9?rik=sa2tHsgZxM0I7g&riu=http%3a%2f%2fwww.yogaensalada.com%2fwp-content%2fuploads%2f2020%2f05%2fLEGS-UP-TO-WALL_1000px_wm-2-831x1024.jpg&ehk=HpWpxGDggnB2Hy7D2FmULle6WCl8Ry595DwnmHXxcnI%3d&risl=&pid=ImgRaw&r=0",
                    "description": "A restorative yoga pose that can help relax and relieve stress while promoting circulation and calming the nervous system."
                },
                {
                    "title": "Seated Forward Bend",
                    "url": "https://yogajala.com/wp-content/uploads/2022/11/seated-forward-fold-pose.jpg",
                    "description": "A gentle stretch for the spine and hamstrings, aiding in relieving tension and enhancing flexibility."
                },
                {
                    "title": "Cobra Pose",
                    "url": "https://omstars.com/blog/wp-content/uploads/2023/07/ig-feed-pose-breakdown-Bhujangasana-Cobra-Pose.png",
                    "description": "A backbend that opens the chest and strengthens the spine, promoting emotional upliftment and vitality."
                }
            ]
        },
        "bored": {
            "songs": [
                {"title": "Balam Pichkari", "url": "https://music.youtube.com/watch?v=d3nBjAuBmME&si=DdroIbAuHJiNlkQp"},
                {"title": "Sunday Best", "url": "https://music.youtube.com/watch?v=WlrzHVMyrjg&si=DipEOx3YNbxN9BzK"},
                {"title": "Good Time", "url": "https://music.youtube.com/watch?v=zGipbUYrUCQ&si=Gse4TrMq3fbBUPnG"},
                {"title": "The Hook Up Song", "url":"https://music.youtube.com/watch?v=6SIe_xz7sKo&si=VHFDQ2d83KIFwXG5"},
                {"title": "Sooraj Dooba Hain", "url":"https://music.youtube.com/watch?v=kbvceIA2Lz4&si=Z-xuBTxOsk3mg5oM"}
            ],
            "books": [
                {
                    "title": "The Hitchhiker's Guide to the Galaxy",
                    "url": "https://www.amazon.in/Fault-our-Stars-John-Green/dp/0141345659/ref=sr_1_1?adgrpid=1328211656176382&dib=eyJ2IjoiMSJ9.D8B9pw2QWoulorAIhS_PdlpVZkCj_MNLB0J9ZHHn3ZsKYHsNqXEO8m0VhRKdbpZdJCVq6zjoQLlkoAERep7018euxT_S-2nmXSRslhUHjSMBD-iTn95gM15H_RaybznevHhkPVqIpWL1JZsxVied9iOG2Q2GcZjT84byznEHsC2EHKkzutBeuMKvLbUmPS7jm4BXSIAL25bchT53-n7a9BjfEyzPyq8wEbmNSBKUsF4.qGAeulx8zQLxjULlU862v8xKCJuMCTkETHmw3tRQyt4&dib_tag=se&hvadid=83013487455319&hvbmt=bb&hvdev=c&hvlocphy=143880&hvnetw=o&hvqmt=p&hvtargid=kwd-83014111398805%3Aloc-90&hydadcr=24870_2165683&keywords=the+fault+in+our+stars&msclkid=5d5fe97265b51de8d6698e61db1521e3&qid=1729347251&s=books&sr=1-1",
                    "description" : "A hilarious sci - fi adventure about Arthur Dent’s journey through space after Earth is destroyed.A mix of wit, humor, and absurdity that’ll keep you entertained."
                },
                {

                    "title": "All the Bright Places",
                    "url": "https://www.amazon.in/All-Bright-Places-Jennifer-Niven/dp/0141357037/ref=sr_1_1?crid=6EE1WTZ69CSL&dib=eyJ2IjoiMSJ9.z0DUpoJ6hTvO5u6h-S-krfgIZFz2J3FQ-bepp-kLZTHru8zYAkRb9bhj3zbzW8V-VnCK_8YTOzcea4hGu01tsbuo1OYWU1AKd4zPWkIYvH_pZCkTZYtNGtV9TiK-pGgqSbMZKOXbd3cmf7_xcdtoj7cX_kdnTqP5ZmUo57B1PvjSjRN7CrAWc_0rc8mN4ZqGKDVHqqVpfQPL_r3kA7pex8SDTkjLEcy56owYDGOGelo.BpY0XnLj88rvtL5jp91Asi4-ZyceSM1ciswhSOjS9G0&dib_tag=se&keywords=all+the+bright+places&qid=1729347348&s=books&sprefix=all+the+bright+places%2Cstripbooks%2C309&sr=1-1",
                    "description": "An emotional story of two teenagers dealing with personal pain and mental health challenges, finding comfort and understanding in one another."
                }
            ],
            "movies": [
                {
                   "title": "Zindagi Na Milegi Dobara (2011)",
                   "url":"https://www.youtube.com/watch?v=hfOZxqwHjzk",
                   "description":" A feel-good movie about friendship, adventure, and self-discovery set against a beautiful road trip through Spain."
                },
                {
                   "title": "Kahaani (2012)",
                   "url":"https://youtu.be/dI-C6VYulhY?si=8PzxdUCnwNv3jEEF",
                   "description":"A gripping mystery thriller that will keep you hooked till the very end, with unexpected twists and a strong storyline."
                },
                {
                       "title": "Bhool Bhulaiyaa (2007)",
                        "url":"https://youtu.be/jzYxbnHHhY4?si=vn8NK7R4w5AUNN10",
                        "description":"A suspense thriller with a cat-and-mouse game, guaranteed to keep your attention with its clever narrative."
                },
                {       "title": "baahubali (2015)",
                        "url":"https://www.youtube.com/watch?v=-4l2jLR7Y8Q",
                        "description":"A breezy, feel-good movie about friendship, relationships, and life’s ups and downs, with a timeless appeal."
                },
                {
                       "title": "Yeh Jawaani Hai Deewani (2013)",
                        "url":"https://youtu.be/WiaHoVh4lXc?si=pDgjopxKDb89KvXl",
                        "description":" A fun, energetic film about love, friendship, and chasing your dreams, with lots of catchy songs and beautiful visuals."
                }
            ],
            "yoga": [
                {
                    "title": "Bridge Pose",
                    "url": "https://img.freepik.com/premium-vector/yoga-infographics-woman-doing-bridge-stretch-exercise-benefits-practice-yoga-poses_530733-2816.jpg",
                    "description": "A pose that strengthens the back and opens the chest, helping to boost energy levels and combat boredom."
                },
                {
                    "title": "Tree Pose",
                    "url": "https://th.bing.com/th/id/OIP.fT64cztBP2Vr8ZlQbrlaVQHaLH?rs=1&pid=ImgDetMain",
                    "description": "A balancing pose that improves focus and concentration, while also grounding the body and mind."
                },
                {
                    "title": "Cat-Cow Stretch",
                    "url": "https://static1.squarespace.com/static/5008a3c6c4aa6450352d2303/t/5266c3a2e4b05199f058e896/1382466467357/cat-cow.jpg",
                    "description": "A gentle flow between two poses that warms the body and brings awareness to the spine, invigorating the mind."
                }
            ]
        },
        "angry": {
            "songs": [
                {"title": "Sadda Haq", "url": "https://music.youtube.com/watch?v=y47Bg9RP2dM&si=HB1zoNPih8meUc9x"},
                {"title": "Smells Like Teen Spirit", "url":"https://music.youtube.com/watch?v=ljUtuoFt-8c&si=v_qptsjbheIwL-qn"},
                {"title": "Apna Time Aayega", "url":"https://music.youtube.com/watch?v=UBhXquUhomY&si=_NPHZjyO7uqmNtWX"},
                {"title": "Aarambh Hai Prachand", "url":"https://music.youtube.com/watch?v=1XFq4tgqJ5g&si=_eGkAU1eVnvHVjxq"},
                {"title": "Stronger", "url":"https://music.youtube.com/watch?v=12hLNbXKCs4&si=-HKWrHUcV5v017Lj"}
            ],
            "books": [
                {
                    "title": "The Fault in Our Stars",
                    "url": "https://www.amazon.in/Fault-our-Stars-John-Green/dp/0141345659/ref=sr_1_1?adgrpid=1328211656176382&dib=eyJ2IjoiMSJ9.D8B9pw2QWoulorAIhS_PdlpVZkCj_MNLB0J9ZHHn3ZsKYHsNqXEO8m0VhRKdbpZdJCVq6zjoQLlkoAERep7018euxT_S-2nmXSRslhUHjSMBD-iTn95gM15H_RaybznevHhkPVqIpWL1JZsxVied9iOG2Q2GcZjT84byznEHsC2EHKkzutBeuMKvLbUmPS7jm4BXSIAL25bchT53-n7a9BjfEyzPyq8wEbmNSBKUsF4.qGAeulx8zQLxjULlU862v8xKCJuMCTkETHmw3tRQyt4&dib_tag=se&hvadid=83013487455319&hvbmt=bb&hvdev=c&hvlocphy=143880&hvnetw=o&hvqmt=p&hvtargid=kwd-83014111398805%3Aloc-90&hydadcr=24870_2165683&keywords=the+fault+in+our+stars&msclkid=5d5fe97265b51de8d6698e61db1521e3&qid=1729347251&s=books&sr=1-1",
                    "description": "A story about love and life in the face of terminal illness, this novel by John Green emphasizes emotional resilience even in the most difficult times."
                },
                {
                    "title": "All the Bright Places",
                    "url": "https://www.amazon.in/All-Bright-Places-Jennifer-Niven/dp/0141357037/ref=sr_1_1?crid=6EE1WTZ69CSL&dib=eyJ2IjoiMSJ9.z0DUpoJ6hTvO5u6h-S-krfgIZFz2J3FQ-bepp-kLZTHru8zYAkRb9bhj3zbzW8V-VnCK_8YTOzcea4hGu01tsbuo1OYWU1AKd4zPWkIYvH_pZCkTZYtNGtV9TiK-pGgqSbMZKOXbd3cmf7_xcdtoj7cX_kdnTqP5ZmUo57B1PvjSjRN7CrAWc_0rc8mN4ZqGKDVHqqVpfQPL_r3kA7pex8SDTkjLEcy56owYDGOGelo.BpY0XnLj88rvtL5jp91Asi4-ZyceSM1ciswhSOjS9G0&dib_tag=se&keywords=all+the+bright+places&qid=1729347348&s=books&sprefix=all+the+bright+places%2Cstripbooks%2C309&sr=1-1",
                    "description": "A profound exploration of mental illness and recovery, this novel by Jennifer Niven tells the story of healing through connection and self-discovery."
                }
            ],
            "movies": [
                {
                    "title": "Dangal (2016)",
                    "url": "https://www.youtube.com/watch?v=aUslLNCEpcc",
                    "description":"A powerful film about determination and fighting against the odds, with intense wrestling scenes that can help you channel your emotions."
                },
                {
                    "title": "Gully Boy (2019)",
                    "url": "https://www.youtube.com/watch?v=IxdLx6zKPwo",
                    "description": "A story of rage transformed into creative energy through music, following a young rapper from the streets of Mumbai fighting to achieve his dreams."
                },
                {
                    "title": "Dabangg 3 (2019)",
                    "url": "https://www.youtube.com/watch?v=3y6zcxVupiA",
                    "description": "Dabangg 3 is a 2019 Bollywood action-comedy film starring Salman Khan, exploring Chulbul Pandey's origins and his fight against a ruthless antagonist. "
                },
                {
                    "title": "Agneepath (2012)",
                    "url": "https://www.youtube.com/watch?v=erjxRyx8gfY",
                    "description": "A revenge-driven drama with high-octane action sequences that can match your intensity when you're angry."
                },
                {
                    "title": "Race 3 (2018)",
                    "url": "https://www.youtube.com/watch?v=XVa-lVHt7_U",
                    "description": "Race 3 is a 2018 Bollywood action-thriller known for its high-octane stunts and an ensemble cast, but it received mixed reviews for its plot and execution."
                }
            ],
            "yoga": [
                {
                    "title": "Mountain Pose",
                    "url": "https://th.bing.com/th/id/OIP.lkhWtFMRn6g46pLnBiLHcQHaHa?rs=1&pid=ImgDetMain",
                    "description": "A basic standing pose that improves posture, balance, and focus."
                },
                {
                    "title": "Tree Pose",
                    "url": "https://th.bing.com/th/id/OIP.fT64cztBP2Vr8ZlQbrlaVQHaLH?rs=1&pid=ImgDetMain",
                    "description": "A balancing pose that strengthens legs, improves focus, and promotes stability."
                },
                {
                    "title": "Cobra Pose",
                    "url": "https://omstars.com/blog/wp-content/uploads/2023/07/ig-feed-pose-breakdown-Bhujangasana-Cobra-Pose.png",
                    "description": "A backbend that opens the chest and strengthens the spine, promoting emotional upliftment and vitality."
                }
            ]
        }
    }

    return content.get(emotion.lower(), "Emotion not found")


# Example usage
emotion = "angry"  # Can be 'happy', 'sad', or 'angry'
recommended_content = recommend_content(emotion)

# Print the recommended content for the chosen emotion
print(recommended_content)