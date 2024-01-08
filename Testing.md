# Full Testing

## Contents
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

## Validator Testing

### HTML

### CSS

### JavaScript

### Python

## Lighthouse Testing

### Performance

### Accessibility

### Best Practises

### SEO

## User Stories

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

