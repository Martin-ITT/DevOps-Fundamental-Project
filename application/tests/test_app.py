# Import the necessary modules
import os
from flask import url_for
from flask_testing import TestCase

# import the app's classes and objects
from application import app, db
from application.models import Students, Tutors, Modules, Enrolments
from datetime import date

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        # if we're testing CRUD functionality with a database, we should
        # configure the application to interact with a test database rather than our production database
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test_data.db",
                SECRET_KEY=os.environ.get("SECRET_KEY"),
                # Ensures the application provides debugging information when errors occur
                DEBUG=True,
                # Testing applications that use WTForms can cause issues with CSRF form validation
                WTF_CSRF_ENABLED=False
                )
        return app

    # Will be called before every test
    def setUp(self):
        # Create table
        db.create_all()
        # Create test registree
        
        student = Students(student_fname = 'Testfname',
        student_lname = 'Testlname',
        student_address1 = 'address1',
        student_address2 = 'address2',
        student_city = 'city',
        student_county = 'county',
        student_phone =  '12345678',
        student_DOB = date(year = 2000, month= 1, day= 1),
        student_email = 'john@doe.com',
        student_password_ff = 'pbkdf2:sha512:52000$JwTTeoU3pUAIvApF$7d9fd2c5abe989653c4f09dce2b1252ddcbc1a4eb37041d3c26ee0b3a49c6c60e7a0a85908abfbab900a2e27a1f06dd3590d1e76aa9639e49f569502bc92be5f',
        authority_lvl = 0)

        tutor = Tutors(tutor_fname = 'Testfname',
        tutor_lname = 'Testlname',
        tutor_address1 = 'address1 ',
        tutor_address2 = 'address2 ',
        tutor_city = 'city',
        tutor_county = 'county',
        tutor_phone =  "12345678",
        tutor_DOB = date(year = 1960, month=1, day=1),
        tutor_email = 'john@doe.com',
        tutor_password_ff = 'pbkdf2:sha512:52000$JwTTeoU3pUAIvApF$7d9fd2c5abe989653c4f09dce2b1252ddcbc1a4eb37041d3c26ee0b3a49c6c60e7a0a85908abfbab900a2e27a1f06dd3590d1e76aa9639e49f569502bc92be5f',
        authority_lvl = 2)

        module = Modules(module_name = 'module ',
        m_tutor_id = 1,
        description = 'description')

        enrolment = Enrolments(enrol_student_id = 1,
        enrol_module_id = 1,
        academic_year = date(year=2022, month=9, day=1),
        ca1_score = 100,
        ca2_score = 75,
        exam_score = 50)

        # save users to database
        db.session.add(student)
        db.session.add(tutor)
        db.session.add(module)
        db.session.add(enrolment)
        db.session.commit()

    # Will be called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()

# Write a test class to test Read functionality
class TestViews(TestBase):
        # Given the Flask is configured properly
    def test_home_get(self):
        # When the home page is requested
        response = self.client.get(url_for('home'))
        # Then check the response is valid - 200
        self.assertEqual(response.status_code, 200)

        # Given the Flask is configured properly, # When the student register page is requested
        # Then valid response is returned
    def test_student_register(self):
        response = self.client.get(url_for('student_register'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the tutor register page is requested
        # Then valid response is returned
    def test_tutor_register(self):
        response = self.client.get(url_for('tutor_register'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the student login page is requested
        # Then valid response is returned
    def test_student_login(self):
        response = self.client.get(url_for('student_login'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the tutor login page is requested
            # Then valid response is returned
    def test_tutor_login(self):
        response = self.client.get(url_for('tutor_login'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the (student) profile page is requested
            #and no user is logged in
                # Then request is denied
    def test_profile(self):
        response = self.client.get(url_for('profile'))
        self.assertEqual(response.status_code, 400)

    # Given the Flask is configured properly, # When the tutor profile page is requested
            #and no user is logged in
                # Then request is denied
    def test_tutor_profile(self):
        response = self.client.get(url_for('tutor_profile'))
        self.assertEqual(response.status_code, 400)

    # Given the Flask is configured properly, # When the logout route is requested
            #and no user is logged in
                # Then request is denied
    def test_logout(self):
        response = self.client.get(url_for('logout'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the update student profile route is requested
            #and student is logged in
                # Then page with a form is returned
    def test_update_student_profile(self):
        response = self.client.get(url_for('update_student_profile'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the update tutor profile route is requested
            #and tutor is logged in
                # Then page with is returned
    def test_update_tutor_profile(self):
        response = self.client.get(url_for('update_tutor_profile'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the student management route is requested
            #and tutor is logged in
                # Then page with a form is returned
    def test_student_management(self):
        response = self.client.get(url_for('student_management'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the delete student route is requested
            #and tutor is not logged in
                # Then page with is returned
    def test_delete_student(self):
        response = self.client.get(url_for('delete_student'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the admin_add_student route is requested
            #and tutor is logged in
                # Then page with a form is returned
    def test_admin_add_student(self):
        response = self.client.get(url_for('admin_add_student'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the admin_add_tutor route is requested
            #and tutor is logged in
                # Then page with a form is returned
    def test_admin_add_tutor(self):
        response = self.client.get(url_for('admin_add_tutor'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the tutor_management route is requested
            #and admin is logged in
                # Then page with a form is returned
    def test_tutor_management(self):
        response = self.client.get(url_for('tutor_management'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the delete_tutor route is requested
            #and admin is logged in
                # Then request is successfull
    def test_delete_tutor(self):
        response = self.client.get(url_for('delete_tutor'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the modules_management route is requested
            #and admin is logged in
                # Then page is returned
    def test_modules_management(self):
        response = self.client.get(url_for('modules_management'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the admin_add_module route is requested
            #and admin is logged in
                # Then page with a is returned
    def test_admin_add_module(self):
        response = self.client.get(url_for('admin_add_module'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the update_module route is requested
            #and admin is logged in
                # Then page with a is returned
    def test_update_module(self):
        response = self.client.get(url_for('update_module'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the delete_module route is requested
            #and admin is logged in
                # Then record is deleted
    def test_delete_module(self):
        response = self.client.get(url_for('delete_module'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the student_grades_check route is requested
            #and student is logged in
                # Then a page is returned
    def test_student_grades_check(self):
        response = self.client.get(url_for('student_grades_check'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the tutor_grades route is requested
            #and tutor is logged in
                # Then a page is returned
    def test_tutor_grades(self):
        response = self.client.get(url_for('tutor_grades'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the tutor_update_grades route is requested
            #and tutor is logged in
                # Then a page with a form is returned
    def test_tutor_grades(self):
        response = self.client.get(url_for('tutor_update_grades'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the enrolment_management route is requested
            #and admin is logged in
                # Then a page with a form is returned
    def test_enrolment_management(self):
        response = self.client.get(url_for('enrolment_management'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the 404 / page_not_found error is returned
                # Then a errorhandling page is returned
    def test_page_not_found(self):
        response = self.client.get(url_for('@app.errorhandler(404)'))
        self.assertEqual(response.status_code, 200)

    # Given the Flask is configured properly, # When the 500 / server_error error is returned
                # Then a errorhandling page is returned
    def test_server_error(self):
        response = self.client.get(url_for('@app.errorhandler(500)'))
        self.assertEqual(response.status_code, 200)


# A test to test the add to DB functionality
class TestAdd(TestBase):
    def test_student_register(self):
        # register new student
        response = self.client.post(
            url_for('student_register'),
            data = dict(student_fname="FakeName",
            student_lname = 'Testlname',
            student_address1 = 'address1',
            student_address2 = 'address2',
            student_city = 'city',
            student_county = 'county',
            student_phone =  '12345678',
            student_DOB = date(year = 2000, month= 1, day= 1),
            student_email = 'john@doe.com',
            student_password_ff = 'f',
            authority_lvl = 0))
        # test that the newly-added student has a correct fname value
        assert Students.query.filter_by(student_fname="FakeName").first == 'FakeName'

    def test_tutor_register(self):
        # register new tutor
        response = self.client.post(
            url_for('tutor_register'),
            data = dict(tutor_fname="FakeName",
            tutor_lname = 'Testlname',
            tutor_address1 = 'address1',
            tutor_address2 = 'address2',
            tutor_city = 'city',
            tutor_county = 'county',
            tutor_phone =  '12345678',
            tutor_DOB = date(year = 2000, month= 1, day= 1),
            tutor_email = 'john@doe.com',
            tutor_password_ff = 'f',
            authority_lvl = 0))
        # test that the newly-added tutor has a correct fname value
        assert Tutors.query.filter_by(tutor_fname="FakeName").first == 'FakeName'

    def test_admin_add_module(self):
        # add new module to db
        response = self.client.post(
            url_for('admin_add_module'),
            data = dict(module = Modules(module_name = 'new_name',
                description = 'new_description',
                m_tutor_id = 2)))
        # test that the newly-added module has an id value of 2,
        # as it's the second record that's been added to the database
        # after 'module' in the setUp() method
        assert Modules.query.filter_by(module_name="new_name").id == 2

    def test_enrolment_management(self):
        # create new enrolment
        response = self.client.post(
            url_for('admin_add_module'),
            data = dict(enrol_student_id = 1,
            enrol_module_id = 1,
            academic_year = date(year=2022, month=9, day=1)))
        # test that the newly-added enrolment tutor has an id value of 2,
        # as it's the second record that's been added to the database
        # after the first in the setUp() method
        assert Enrolments.query.filter_by(module_name="new_name").id == 2
