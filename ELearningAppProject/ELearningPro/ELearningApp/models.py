from django.db import models
class Category(models.Model):
	category_title = models.CharField(max_length=50)
	def __str__(self):
		return (self.category_title)

class Tag(models.Model):
	tag_title = models.CharField(max_length = 50)
	def __str__(self):
		return (self.tag_title)

class Course(models.Model):
	course_category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag)
	course_title = models.CharField(max_length = 50)
	course_price = models.IntegerField()
	course_description = models.CharField(max_length = 200)
	course_requirment = models.CharField(max_length = 200)
	url_link = models.URLField(max_length = 500)
	STATUS = (
		("draft","Draft"),
		("published","Published")
		)
	status_choices = models.CharField(max_length = 50, choices=STATUS, default="draft")
	def __str__(self):
		return (self.course_title)


class CourseCurriculam1(models.Model):
	AddCourse = models.ForeignKey(Course, on_delete=models.CASCADE)
	Headings = models.CharField(max_length = 500)
	def __str__(self):
		return (self.Headings)

class CourseCurriculam2(models.Model):
	AddCourseCurriculam1 = models.ForeignKey(CourseCurriculam1, on_delete=models.CASCADE)
	Headings= models.CharField(max_length = 500)
	video = models.FileField()
	def __str__(self):
		return (self.Headings)

class QuizeTitle(models.Model):
	CourseQuizeTitle = models.ForeignKey(Course, on_delete=models.CASCADE)
	quize_title = models.CharField(max_length=100)
	def __str__(self):
		return (self.quize_title)


class Questions(models.Model):
	AddQuizeTitle=models.ForeignKey(QuizeTitle, on_delete=models.CASCADE)
	question = models.TextField(max_length=500)
	CHOICES = (
		("Single_Answer" , "SINGLE"),
		("Multi_Answer" , "MULTI"),
		("Dragula_Answer" , "DRAGULA")
		)
	type_of_ans =models.CharField(max_length =50 ,choices  = CHOICES, default = "Single_Answer") 
	def __str__(self):
		return (self.question)

class Answers(models.Model):
	AddQuestions=models.ForeignKey(Questions, on_delete=models.CASCADE)
	ans_no=models.IntegerField()
	ans = models.TextField(max_length=500)
	Decision = (
		("wrong","wrong"),
		("right","right")
		)
	wrong_or_right= models.CharField(max_length=100, choices=Decision, default="wrong")
	def __str__(self):
		return (self.ans)

