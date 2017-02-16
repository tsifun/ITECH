from django.test import TestCase


from django.core.urlresolvers import reverse


from django.contrib.staticfiles import finders

4

5  # Thanks to Enzo Roiz https://github.com/enzoroiz who made these tests during an internship with us
6

7


class GeneralTests(TestCase):
    8

    def test_serving_static_files(self):

        9  # If using static media properly result is not NONE once it finds rango.jpg


10
result = finders.find('images/rango.jpg')
11
self.assertIsNotNone(result)
12

13

14


class IndexPageTests(TestCase):
    15


16


def test_index_contains_hello_message(self):
    17  # Check if there is the message 'Rango Says'


18  # Chapter 4
19
response = self.client.get(reverse('index'))
20
self.assertIn(b'Rango says', response.content)
21
22


def test_index_using_template(self):
    23  # Check the template used to render index page


24  # Chapter 4
25
response = self.client.get(reverse('index'))
26
self.assertTemplateUsed(response, 'rango/index.html')
27

28


def test_rango_picture_displayed(self):
    29  # Check if is there an image called 'rango.jpg' on the index page


30  # Chapter 4
31
response = self.client.get(reverse('index'))
32
self.assertIn(b'img src="/static/images/rango.jpg', response.content)
33
34


def test_index_has_title(self):
    35  # Check to make sure that the title tag has been used


36  # And that the template contains the HTML from Chapter 4
37
response = self.client.get(reverse('index'))
38
self.assertIn(b'<title>', response.content)
39
self.assertIn(b'</title>', response.content)
40

41

42


class AboutPageTests(TestCase):
    43


44


def test_about_contains_create_message(self):
    45  # Check if in the about page is there - and contains the specified message


46  # Exercise from Chapter 4
47
response = self.client.get(reverse('about'))
48
self.assertIn(b'This tutorial has been put together by', response.content)
49
50
51


def test_about_contain_image(self):
    52  # Check if is there an image on the about page


53  # Chapter 4
54
response = self.client.get(reverse('about'))
55
self.assertIn(b'img src="/static/images/', response.content)
56
57


def test_about_using_template(self):
    58  # Check the template used to render index page


59  # Exercise from Chapter 4
60
response = self.client.get(reverse('about'))
61

62
self.assertTemplateUsed(response, 'rango/about.html')
63
64
65
66


class ModelTests(TestCase):
    67


68


def setUp(self):
    69
    try:
        70
    from populate_rango import populate


71
populate()
72         except ImportError:
73
print('The module populate_rango does not exist')
74         except NameError:
75
print('The function populate() does not exist or is not correct')
76         except:
77
print('Something went wrong in the populate() function :-(')
78
79
80


def get_category(self, name):
    81


82
from rango.models import Category

83
try:
    84
    cat = Category.objects.get(name=name)
85         except Category.DoesNotExist:
86
cat = None
87
return cat
88
89


def test_python_cat_added(self):
    90
    cat = self.get_category('Python')


91
self.assertIsNotNone(cat)
92
93


def test_python_cat_with_views(self):
    94
    cat = self.get_category('Python')


95
self.assertEquals(cat.views, 128)
96
97


def test_python_cat_with_likes(self):
    98
    cat = self.get_category('Python')


99
self.assertEquals(cat.likes, 64)
100
101

102


class Chapter4ViewTests(TestCase):
    103

    def test_index_contains_hello_message(self):

        104  # Check if there is the message 'hello world!'


105
response = self.client.get(reverse('index'))
106
self.assertIn('Rango says', response.content)
107

108


def test_does_index_contain_img(self):
    109  # Check if the index page contains an img


110
response = self.client.get(reverse('index'))
111
self.assertIn('img', response.content)
112

113


def test_about_using_template(self):
    114  # Check the template used to render index page


115  # Exercise from Chapter 4
116
response = self.client.get(reverse('about'))
117

118
self.assertTemplateUsed(response, 'rango/about.html')
119

120


def test_does_about_contain_img(self):
    121  # Check if in the about page contains an image


122
response = self.client.get(reverse('about'))
123
self.assertIn('img', response.content)
124

125


def test_about_contains_create_message(self):
    126  # Check if in the about page contains the message from the exercise


127
response = self.client.get(reverse('about'))
128
self.assertIn('This tutorial has been put together by', response.content)
129

130

131


class Chapter5ViewTests(TestCase):
    132


133


def setUp(self):
    134
    try:
        135
    from populate_rango import populate


136
populate()
137         except ImportError:
138
print('The module populate_rango does not exist')
139         except NameError:
140
print('The function populate() does not exist or is not correct')
141         except:
142
print('Something went wrong in the populate() function :-(')
143

144

145


def get_category(self, name):
    146


147
from rango.models import Category

148
try:
    149
    cat = Category.objects.get(name=name)
150         except Category.DoesNotExist:
151
cat = None
152
return cat
153

154


def test_python_cat_added(self):
    155
    cat = self.get_category('Python')


156
self.assertIsNotNone(cat)
157

158


def test_python_cat_with_views(self):
    159
    cat = self.get_category('Python')


160

161
self.assertEquals(cat.views, 128)
162

163


def test_python_cat_with_likes(self):
    164
    cat = self.get_category('Python')


165
self.assertEquals(cat.likes, 64)
166

167


def test_view_has_title(self):
    168
    response = self.client.get(reverse('index'))


169

170  # Check title used correctly
171
self.assertIn('<title>', response.content)
172
self.assertIn('</title>', response.content)
173

174  # Need to add tests to:
175  # check admin interface - is it configured and set up
176

177


def test_admin_interface_page_view(self):
    178
    from admin import PageAdmin


179
self.assertIn('category', PageAdmin.list_display)
180
self.assertIn('url', PageAdmin.list_display)
181

182

183


class Chapter6ViewTests(TestCase):
    184


185


def setUp(self):
    186
    try:
        187
    from populate_rango import populate


188
populate()
189         except ImportError:
190
print('The module populate_rango does not exist')
191         except NameError:
192
print('The function populate() does not exist or is not correct')
193         except:
194
print('Something went wrong in the populate() function :-(')
195

196

197  # are categories displayed on index page?
198

199  # does the category model have a slug field?
200

201

202  # test the slug field works..
203


def test_does_slug_field_work(self):
    204
    from rango.models import Category


205
cat = Category(name='how do i create a slug in django')
206
cat.save()
207
self.assertEqual(cat.slug, 'how-do-i-create-a-slug-in-django')
208

209  # test category view does the page exist?
210

211

212  # test whether you can navigate from index to a category page
213

214

215  # test does index page contain top five pages?
216

217  # test does index page contain the words "most liked" and "most viewed"
218

219  # test does category page contain a link back to index page?
220

221

222


class Chapter7ViewTests(TestCase):
    223


224


def setUp(self):
    225
    try:
        226
    from forms import PageForm


227
from forms import CategoryForm

228

229         except ImportError:
230
print('The module forms does not exist')
231         except NameError:
232
print('The class PageForm does not exist or is not correct')
233         except:
234
print('Something else went wrong :-(')
235

236
pass
237  # test is there a PageForm in rango.forms
238

239  # test is there a CategoryForm in rango.forms
240

241  # test is there an add page page?
242

243  # test is there an category page?
244

245

246  # test if index contains link to add category page
247  # <a href="/rango/add_category/">Add a New Category</a><br />
248

249

250  # test if the add_page.html template exists.
