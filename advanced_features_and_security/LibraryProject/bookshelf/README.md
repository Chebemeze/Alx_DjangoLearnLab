This project focuses on creating customized permissions for a model
It implements the use of assigning these permissions to groups. Finally assigning users to this groups.
The significance of this is that when the model increases we dont have to select
the various permissions the model should have rather we just assign them to a group which has the permission they require.

To do this:
1. create a Meta class (class Meta:) of any model you want to create permissions for.
2. Utilize @permission_required (@permission_required ('app_name.codename', raise_exception= False)) decorators to protect the functions that will be responsible for what the permisiions/actions that you want to assign will behave.
3. Create urls to navigate to the various permissions handled in view when the urls are typed in a browser.
4. Register the model in admin.py so it shows up in django admin UI.
5. Create a class in admin to modify the registered class in step 4. what this
does it that specifies how field in the model will be serched, displayed, and filtered. The most important reason of creating this class is to enable django admin to use your customized permission instead of the default permission it created during the creation of your model.