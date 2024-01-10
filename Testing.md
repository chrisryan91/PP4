# Full Testing

## Contents
- Testing User Stories
- Validator Testing
- HTML Testing
- CSS Testing
- JavaScript Testing
- Python Testing
- User Stories Testing
- Automated Testing
- Manual Testing
- Responsive Testing
- Bugs and Fixes
- Known Bugs

## Testing User Stories

User Stories were created at the start of my project. I did not check on in them enough

## User Story 1

- As a site administrator I can create, read, update and delete so that the blog's content can be managed

I copied the Code Institute template and got my environment set up - i.e installing Django - I created a superuser and was able to access admin on my Django project. This allows the admin to perform CRUD functionality.

<details>
<summary>User Story 1</summary>
<br>

![User Story 1](static/readme_images/UserStoryTesting/ust1.png)
</details>

## User Story 2

- As a site user I can use the search the recipe blog so that I can find recipes

After setting up base.html, index.html and search.html, I set up use of EDAMAM API in settings. I had to add some environment variables with my API_KEY and API_ID. Unlike most of my views in views.py, my search view is a function based view. This allowed me to make an API call with an input field in the search page which returned recipes on the same page. I used Django templating language to render the returned recipes. This allows the user to enter a value and receive recipes.

<details>
<summary>User Story 2</summary>
<br>

```
def SubmitReview(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ReviewForm(request.POST, request.FILES)
            if form.is_valid():
                review = form.save(commit=False)
                review.author = request.user
                review.save()
                form.save_m2m()

                existing_ingredients = form.cleaned_data.get('ingredients')
                review.ingredients.set(existing_ingredients)

                new_ingredient_string = form.cleaned_data.get('new_ingredient', '')
                new_ingredient_list = [
                    ingredient.strip()
                    for ingredient in new_ingredient_string.split(',')]

                for new_ingredient_name in new_ingredient_list:
                    try:
                        new_ingredient, created = Ingredient.objects.get_or_create(
                            name=new_ingredient_name)
                        review.ingredients.add(new_ingredient)
                    except IntegrityError:
                        try:
                            new_ingredient = Ingredient.objects.get(
                                name=new_ingredient_name)
                        except Ingredient.DoesNotExist:
                            new_ingredient_id = Ingredient.objects.latest(
                                'id').id + 1
                            new_ingredient = Ingredient.objects.create(
                                id=new_ingredient_id, name=new_ingredient_name)
                        review.ingredients.add(new_ingredient)

                if review.featured_image_a:
                    print(f"Cloudinary URL: {review.featured_image_a.url}")
                else:
                    print("No Cloudinary URL available (featured_image_a is None)")

                url = form.cleaned_data.get("url")
                if url:
                    request.session["modalURL"] = url
                    print(f"Session modalURL set to: {url}")

                return redirect('review_blog')
            else:
                print(form.errors)
        else:
            form = ReviewForm()
            print(form.errors)

        return render(request, 'submit_review.html', {
            'form': form,
            'ingredients': Ingredient.objects.all(),
            'utensils': Utensil.objects.all()})
    
    else:
        return redirect('login')
```
</details>

## User Story 3

- As a user I can search with ingredients, tag names or cuisine type so that I can see a list of recipes.
  
To make an API call I needed to input a string of comma separated values. This was not user friendly. I wanted users to be able to search with tags with ingredients or cuisine types. I found [select2](https://select2.org/) which "gives you a customizable select box with support for searching, tagging, remote data sets, infinite scrolling, and many other highly used options." It allowed for users to enter single ingredients or other tags which could be converted into a comma separated string to make the API call. This allows the user to search by ingredient or other tag names.


<details>
<summary>User Story 3 JavaScript</summary>
<br>

```
$(document).ready(function () {
    $('#id_ingredients').select2();

    $('#id_utensils').select2();

    $('#id_cuisine_type').select2();
});
```
</details>

<details>
<summary>User Story 3 JavaScript</summary>
<br>

```
$(document).ready(function () {
    $('#id_ingredients').select2();

    $('#id_utensils').select2();

    $('#id_cuisine_type').select2();
});

$(document).ready(function() {
    $('#ingredientInput').select2({
        tags: true,
        tokenSeparators: [','],
        placeholder: 'Enter ingredients',
    });

    $('form').submit(function() {
        var selectedIngredients = $('#ingredientInput').val();
        $('#ingredientQuery').val(selectedIngredients.join(','));
    });
})
```
</details>

<details>
<summary>User Story 3 View</summary>
<br>

```
class SearchForm(forms.Form):
    query = forms.CharField(
        validators=[
            RegexValidator(
                regex="^[a-zA-Z, ]+$",
                message="Only letters, commas, and spaces are allowed."
            )]
    )
```
</details>

## User Story 4

- As a site user I can view a list of paginated recipes so that select the recipe details

I looked for different methods of displaying recipes in repeating card. I was going to go ahead and use infinite scroll but because I had experience using pagination I decided to use Django pagination in order to create an end to the amount of rows on each html page before the user is prompted to click "next". This would create a "next" page, "last" page, "previous" page and "first" page rendered after a specific amount of recipes are rendered. This allows the user to click through pages.


<details>
<summary>User Story 5</summary>
<br>

```        
{% if is_paginated %}
        <nav aria-label="Page navigation" class="pag-nav">
            <ul class="pagination justify-content-center">
                {% if page_obj.has_previous %}
                <li><a href="?page={{ page_obj.previous_page_number }}" class="page-link">&laquo; PREV</a></li>
                {% endif %}
                {% if page_obj.has_next %}
                <li><a href="?page={{ page_obj.next_page_number }}" class="page-link">NEXT &raquo;</a></li>
                {% endif %}
            </ul>
        </nav>
        {% endif %}
```

## User Story 5

- As a Site User I can click on a recipe so that I can see the details.

For this I needed to create a link one each of the card divisions with a link to the URL. When the user hovers over the div two icons appear with anchor links - to the URL to see the details and to Submit Review. This allows the user to see the details of the specific recipe.

<details>
<summary>User Story 5</summary>
<br>

![User Story 5](static/readme_images/screenshots/reviewhover_img.png)
</details>

## User Story 6

- As a site administrator I can approve or disapprove comments and recipes so that I can filter content

In admin.py, I was able to import the Comment model and all of it's fields. One of this is Approved. Approved is a Boolean value initially set to False. One of the "actions" defined in admin.py is "approve_comments". This allows the administration to approve comments and recipes so content can be filtered.

<details>
<summary>User Story 6</summary>
<br>

```
class Comment(models.Model):
    approved = models.BooleanField(default=False)
```
</details>

<details>
<summary>User Story 6</summary>
<br>

```
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_on', 'approved', 'review')
    list_filter = ('approved', 'created_on', 'review')
    search_fields = ('name', 'address', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
```
</details>

## User Story 7

- As a site user I can see my user profile so that I can see my details

This user story was never completed as intended. Initially I wanted to have a user profile dashboard to achieve CRUD functionality. Rather than that, users are given the option to perform CRUD operations on their own posts on the review blog.

## User Story 8

- As a site user I can register an account so that I can leave a comment, rating and like

I used [Django All Auth](https://docs.allauth.org/en/latest/) to authenticate users. There is a signup, login and logout pages with forms to handle entry of user details. Only authenticated users can comment, upvote and leave a review so this gives users the ability to register.

<details>
<summary>User Story 8 Screenshot</summary>
<bn>

![User Story 8](static/readme_images/screenshots/signup_lg.png)
</details>

<details>
<summary>User Story 8 Code</summary>
<br>

```
class CustomSignupView(SignupView):
    template_name = 'account/signup.html'
    form_class = CustomSignupForm

class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = CustomLoginForm`
```
</details>


## User Story 9

- As a user I can submit recipe reviews so that I can add a recipe review to the blog

A submit review page is available to only authenticated users where they can fill out a form to submit a review. Again this is handled by a function based view. It has fields that correspond to the Review model. This allows users to submit a review - and if it passes review by the admin it will be published.

<details>
<summary>User Story 9 Screenshot</summary>
<br>

![User Story 9](static/readme_images/screenshots/submitreview_img.png)
</details>

<details>
<summary>User Story 9 View</summary>
<br>

```
def SubmitReview(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ReviewForm(request.POST, request.FILES)
            if form.is_valid():
                review = form.save(commit=False)
                review.author = request.user
                review.save()
                form.save_m2m()

                existing_ingredients = form.cleaned_data.get('ingredients')
                review.ingredients.set(existing_ingredients)

                new_ingredient_string = form.cleaned_data.get('new_ingredient', '')
                new_ingredient_list = [
                    ingredient.strip()
                    for ingredient in new_ingredient_string.split(',')]

                for new_ingredient_name in new_ingredient_list:
                    try:
                        new_ingredient, created = Ingredient.objects.get_or_create(
                            name=new_ingredient_name)
                        review.ingredients.add(new_ingredient)
                    except IntegrityError:
                        try:
                            new_ingredient = Ingredient.objects.get(
                                name=new_ingredient_name)
                        except Ingredient.DoesNotExist:
                            new_ingredient_id = Ingredient.objects.latest(
                                'id').id + 1
                            new_ingredient = Ingredient.objects.create(
                                id=new_ingredient_id, name=new_ingredient_name)
                        review.ingredients.add(new_ingredient)

                if review.featured_image_a:
                    print(f"Cloudinary URL: {review.featured_image_a.url}")
                else:
                    print("No Cloudinary URL available (featured_image_a is None)")

                url = form.cleaned_data.get("url")
                if url:
                    request.session["modalURL"] = url
                    print(f"Session modalURL set to: {url}")

                return redirect('review_blog')
            else:
                print(form.errors)
        else:
            form = ReviewForm()
            print(form.errors)

        return render(request, 'submit_review.html', {
            'form': form,
            'ingredients': Ingredient.objects.all(),
            'utensils': Utensil.objects.all()})
    
    else:
        return redirect('login')
```
</details>

## User Story 10

- As a site user and administrator I can view the comments on a recipe so that see what is being talked about

Comments are rendered in the html page underneath the review itself. They can be managed by the administrator in the admin section. If a user is authenticated, they can respond to a comment. If a user is authenticated and the author of a comment, they can delete the comment. This allows the users and admins to view comments and see what is being talked about.

<details>
<summary>User Story 10 Screenshot</summary>
<br>

![User Story 10](static/readme_images/screenshots/reviewcomments_img.png)
</details>

## User Story 11

- As a administrator I can approve posts so that the blog is populated

Similarly to the comment approval User Story above, our Review class has a status model. This is initially set to 0. In the admin section, the administrator can review posts and publish them to the blog with this feature. By setting the "STATUS" to "1" to indicate "Published" allowing the blog to be populate.

<details>
<summary>User Story 11</summary>
<br>

```
STATUS = ((0, "DRAFT"), (1, "Published"))
```
</details>

<details>
<summary>User Story 11 Review Status</summary>
<br>

```
class Review(models.Model):
    status = models.IntegerField(choices=STATUS, default=0)
```
</details>

## User Story 12

- As a site user and administrator I can view the rating and number of likes on each recipe so that I can determine the best and popular ones

I first created two icons - a thumbs up and a thumbs down icon - to signify upvotes. Two forms needed to be added to each icon - and two buttons on each form. Four buttons altogether - one if they have upvoted, one if they have not upvoted, one if they have downvoted, one if they have not downvoted. If the user has upvoted, they can downvote, but the upvote has to be removed. If the user has downvoted, they can upvote, the downvote has to be removed. A class is attached to change the colour of the icon depending on the users choice.

I attached the template and the logic below. This became a bug for me. It is documented in the bugs section. I luckily found a solution on ![Stack Overflow](https://stackoverflow.com/questions/77376229/django-upvote-downvote-system)

<details>
<summary>User Story 12 Upvote Screenshot</summary>
<br>

![User Story 10](static/readme_images/screenshots/123.png)
</details>

<details>
<summary>User Story 12 Template</summary>
<br>

```
    {% if user.is_authenticated %}
        <form class="d-inline" action="{% url 'review_upvote' review.slug %}" method="POST">
            {% csrf_token %}
            <input type="hidden" name="vote_type" value="upvote">
            {% if liked %}
            <button type="submit" name="review_id" value="{{ review.slug }}" class="btn-like">
                    <i class="far fa-thumbs-up upvoted"></i>
            </button>
                {% else %}
            <button type="submit" name="review_id" value="{{ review.slug }}" class="btn-like">
                    <i class="far fa-thumbs-up"></i>
            </button>
                {% endif %}
        </form>
        <form class="d-inline" action="{% url 'review_upvote' review.slug %}" method="POST">
            {% csrf_token %}
            <input type="hidden" name="vote_type" value="downvote">
                {% if disliked %}
                <button type="submit" name="blog_id" value="{{ review.slug }}" id="btn-like" class="btn-like">
                    <i class="far fa-thumbs-down downvoted"></i>
                </button>
                {% else %}
                <button type="submit" name="blog_id" value="{{ review.slug }}" id="btn-like" class="btn-like">
                    <i class="far fa-thumbs-down"></i>
                </button>
                {% endif %}
        </form>
    {% else %}
        <i class="fas fa-thumbs-up"></i>
        <i class="fas fa-thumbs-down"></i>
    {% endif %}
```
</details>

<details>
<summary>User Story 12 Logic</summary>
<br>


```
class ReviewUpvote(View):
    def post(self, request, slug):
        review = get_object_or_404(Review, slug=slug)

        vote_type = request.POST.get('vote_type', None)
        if vote_type == 'upvote':
            review.up_vote.filter(id=request.user.id).exists() is False \
                and review.up_vote.add(request.user)
            review.down_vote.filter(id=request.user.id).exists() \
                and review.down_vote.remove(request.user)

        elif vote_type == 'downvote':
            review.down_vote.filter(id=request.user.id).exists() \
                is False and review.down_vote.add(request.user)
            review.up_vote.filter(id=request.user.id).exists() \
                and review.up_vote.remove(request.user)

        generated_url = reverse('review_post', args=[slug])
        print("Generated URL:", generated_url)

        return HttpResponseRedirect(reverse('review_post', args=[slug]))
```
</details>

## Validator Testing

### HTML

### CSS

I have one single CSS file for the application. It passes through W3S CSS validator.

<details>
<summary>CSS Validation</summary>
<br>

![CSS Validation](static/readme_images/csshtmljsvalid/css.png)
</details>

### JavaScript

There is one single JavaScript file in this project. It passes JSHint. 

<details>
<summary>JavaScript Validation</summary>
<br>

![JavaScript Validation](static/readme_images/csshtmljsvalid/js.png)
</details>

### Python

All my python files are PEP8 compliant. For this, I used the Code Institute Linter. They all passed with no issues. For example:

<details>
<summary>admin.py</summary>
<br>

![Admin.py](static/readme_images/python%20linter/admin%20linter.png)
</details>

<details>
<summary>forms.py</summary>
<br>

![Admin.py](static/readme_images/python%20linter/forms%20linter.png)
</details>

<details>
<summary>models.py</summary>
<br>

![Admin.py](static/readme_images/python%20linter/models%20linter.png)
</details>

<details>
<summary>urls.py</summary>
<br>

![Admin.py](static/readme_images/python%20linter/urls%20linter.png)
</details>

<details>
<summary>views.py</summary>
<br>

![Admin.py](static/readme_images/python%20linter/views%20linter.png)
</details>

## Lighthouse Testing

### Performance

### Accessibility

### Best Practises

### SEO

## Automated Testing

## Manual Testing

### Header

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Site Name| Click | Return to homepage | Works|
| Site Name| Hover | Cursor changes | Works|
| Search Link | Click | Directs to search page | Works|
| Search Link | Hover | Icon Wobbles | Works|
| Search Link | Hover | Cursor changes | Works|
| Reviews Link | Click | Directs to Reviews Blog page | Works|
| Reviews Link | Hover | Icon Wobbles | Works|
| Reviews Link | Hover | Cursor changes | Works|
| About Link | Click | Directs to About page | Works|
| About Link | Hover | Icon Wobbles | Works|
| About Link | Hover | Cursor changes | Works|

If not logged in:

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Register Link | Click | Directs to Register page | Works|
| Register Link | Hover | Icon Wobbles | Works|
| Register Link | Hover | Cursor changes | Works|
| Login Link | Click | Directs to Login page | Works|
| Login Link | Hover | Icon Wobbles | Works|
| Login Link | Hover | Cursor changes | Works|

If logged in:

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Logout Link | Click | Directs to Logout page | Works|
| Logout Link | Hover | Icon Wobbles | Works|
| Logout Link | Hover | Cursor changes | Works|

### Footer

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Facebook Link | Click | Facebook opens in new tab | Works|
| Facebook Link | Hover | Icon Wobbles | Works|
| Facebook Link | Hover | Cursor changes | Works|
| Twitter Link | Click | Twitter opens in new tab | Works|
| Twitter Link | Hover | Icon Wobbles | Works|
| Twitter Link | Hover | Cursor changes | Works|
| Instagram Link | Click | Instagram opens in new tab | Works|
| Instagram Link | Hover | Icon Wobbles | Works|
| Instagram Link | Hover | Cursor changes | Works|
| YouTube Link | Click | YouTube opens in new tab | Works|
| YouTube Link | Hover | Icon Wobbles | Works|
| YouTube Link | Hover | Cursor changes | Works|

### Home Page

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Search Link | Click | Directs to Search page | Works|
| Search Link | Hover | Cursor changes | Works|
| View Blog Link | Click | Directs to Reviews Blog | Works|
| View Blog Link | Hover | Cursor changes | Works|

### Search Page

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Form Input | Enter Ingredient | Select2 targets the element and saves it in a tag | Works |
| Form Button | Enter anything other than a string with letters | Invalid data message | Works |
| Form Button | Click Search with valid | Tags get converted to CSV string and returns recipes | Works |
| Form Button | Click Search with data with no results | "No results" renders in template | Works |

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Card Div | Hover | Div appears with anchored icon | Works |
| Card Div Icon | Hover | Text appears with external link to review | Works |
| Card Div Icon | Click | New tab opens with link to recipe | Works |
| Card Div Icon | Hover | URL, Label, Image stores in sessionStorage | Works |

If logged in:

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Card Div | Hover | Div appears with second anchored icon | Works |
| Card Div Icon | Hover | Text appears with internal link to review recipe | Works |
| Card Div Icon | Click | Redirect to submit review page | Works |

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Next Link | Click | Directs to Next page | Works|
| Last Link | Click | Directs to Last page | Works|

### Submit Review Page

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Title Input | Type/Click | Title will function | Works|
| Recipe Input | Type/Click | Not working - readme only | Works|
| Review Input | Type/Click | Review content appears | Works|
| URL Input | Type/Click | Not working - readme only | Works|
| Cuisine Type Input | Type/Click | Select 2 targets element, creates tags to choose from database | Works|
| Ingredients Input | Type/Click | Select 2 targets element, creates tags to choose from | Works|
| Utensils Input | Type/Click | Select 2 targets element, creates tags to choose from | Works|
| Cloudinary Input | Click choose file | File Explored box pops up to choose image | Works|
| Prep Time Input | Type | Text box appears only allowing numbers | Works |
| New Ingredient Input | Type | Text box appears | Works |

On Submit:

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Cuisine Type Input | Enter Two Values | Valid | Works|
| Ingredients Input | Enter no values | Invalid | Works|
| Utensils Input | Enter no values | Invalid | Works|
| Cloudinary Input | Enter no image | Valid | Works|
| Prep Time Input | Type | Enter no value | Works |
| New Ingredient Input | Enter CSV string | valid | Works |
| New Utensil Input | Enter CSV string | Valid | Works |

### Review List Page

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Sort-By Dropdown | Click | Drop down appears with two values: latest and upvotes | Works|
| Sort-By Button | Click | Card Divs sort themselves correctly | Works|
| Review Card Div | Hover | Div with Icon Appears in Center | Works|
| Review Card Div Icon | Hover | "Visit Review" text appears | Works |
| Next Link | Click | Directs to Next page | Works|
| Last Link | Click | Directs to Last page | Works|

### Review Post Page

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| External Recipe Link | Click | New tab opens with recipe | Works|

If logged in:

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Upvote | Hover | Icon Wobbles | Works|
| Upvote | Click | Colour Changes, total upvotes increases correctly | Works|
| Downvote | Hover | Icon Wobbles | Works|
| Downvote | Click | Colour Changes, total upvotes decreases correctly | Works|
| Comment Textbox | Click/Type | Textbox size can be increased and written in | Works|
| Comment Submit Button | Click | In text is in the box, valid - otherwise, not valid | Works|

If logged in user in Review author:

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Update Review Link | Click | Page redirects to a new form | Works |

### Update Review Page

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Title Input | Type/Click | Text can be updated | Works|
| Recipe Input | Type/Click | Not working - readme only | Works|
| Review Input | Type/Click | Text can be updated | Works|
| URL Input | Type/Click | Not working - readme only | Works|
| Cuisine Type Input | Type/Click | Select 2 targets element, creates tags to choose from database, tags can be delted | Works|
| Ingredients Input | Type/Click | Select 2 targets element, creates tags to choose from, tags can be deleted | Works|
| Utensils Input | Type/Click | Select 2 targets element, creates tags to choose from, tags can be deleted | Works|
| Cloudinary Input | Click choose file | File Explored box pops up to choose image, old image can be cleared | Works|
| Prep Time Input | Type | Text box appears only allowing numbers | Works |
| New Ingredient Input | Type | Text box appears | Works |

On Submit:

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Cuisine Type Input | Enter Two Values | Valid | Works|
| Ingredients Input | Enter no values | Invalid | Works|
| Utensils Input | Enter no values | Invalid | Works|
| Cloudinary Input | Enter no image | Valid | Works|
| Prep Time Input | Type | Enter no value | Works |
| New Ingredient Input | Enter CSV string | valid | Works |
| New Utensil Input | Enter CSV string | Valid | Works | 

### About Page

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| External links | Click | New tab opens with correct link | Works |

### Register Page

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Sign in link | Click | Page redirects to login page | Works |

On submit:

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Name input | Type Name that already exists | Invalid - notification appears appears | Works|
| Name input | Type Name that doesn't exists | Valid | Works|
| Password input | Password Contains Name | Invalid - notification appears appears | Works|
| Password input | Password Doesn't Contains Name | Valid | Works|
| Password input | Paste password into input field | Invalid | Works |
| Email input | No input | Valid | Works|
| Email input | Text but not an email address | Not valid - needs @ | Works|
| Email input | Enter email | Valid | Works |
| Sign-up button | Click | Valid | Works |

### Sign-in Page

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Name Input & Password Input | type | Values appear | Works |
| Remember Me Checkbox | Click | Checkbox ticks | Works |
| Sign In Button | Click with valid data| Logs in | Works |
| Sign In Button | Click with invalid data| Message is rendered in html | Works |

### Logout Page

| Element | Action | Expectation | Result|
|---------|--------|-------------|-------|
| Logout Button | Click | Logs out | Works |

## Responsiveness Testing

## Bugs

### Fixed Bugs

### Known Bugs

