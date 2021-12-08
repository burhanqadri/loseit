filenames = ['heading.txt', 'amended_authors_comments.txt']
# filenames = ['test111.txt', 'test_store_auth_submissions.txt']
# filenames = ['loseit_posts.txt', 'loseit_posts_2.txt', 'loseit_posts_3.txt']
# filenames = ['progresspics_comments.txt', 'progresspics_comments_2.txt']
# filenames = ['progresspics_posts.txt', 'progresspics_posts_2.txt']

with open('authors_comments.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
            outfile.write("\n")
