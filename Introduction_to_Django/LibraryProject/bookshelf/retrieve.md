first_book = Book.objects.all()
<!-- fetches all list of object -->

first_book[0].title, first_book[0].author, first_book[0].publication_year
<!-- Lists the title, author, and publication of the first object in first_book hence the use of index zero -->