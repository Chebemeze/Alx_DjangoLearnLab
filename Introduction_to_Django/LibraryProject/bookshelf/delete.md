first_book = Book.objects.all()
<!-- fetches all list of object -->

first_book[0].delete()
<!-- This deletes records of the first_book -->