first_book = Book.objects.all()
<!-- fetches all list of object -->

first_book[0].title =  "Nineteen Eighty-Four"
first_book[0].save()
<!-- This updates the title from 1984 to Nineteen Eighty-Four and saves to database-->