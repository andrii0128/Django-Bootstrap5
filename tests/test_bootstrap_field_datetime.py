from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime

from tests.base import BootstrapTestCase


class DateTimeTestForm(forms.Form):
    test = forms.SplitDateTimeField(widget=AdminSplitDateTime())


class DateTimeTestCase(BootstrapTestCase):
    def test_input_type_admin_split_date_time(self):
        """Test field with AdminSplitDateTime widget."""
        self.assertHTMLEqual(
            self.render("{% bootstrap_field form.test %}", context={"form": DateTimeTestForm()}),
            (
                '<div class="django_bootstrap5-req mb-3">'
                '<label class="form-label" for="id_test_0">Test</label>'
                '<p class="datetime">'
                "Date: "
                '<input type="text" name="test_0" class="form-control vDateField" size="10"'
                ' placeholder="Test" required id="id_test_0">'
                "<br>"
                "Time: "
                '<input type="text" name="test_1" class="form-control vTimeField" size="8"'
                ' placeholder="Test" required id="id_test_1">'
                "</p>"
                "</div>"
            ),
        )

    def test_input_type_admin_split_date_time_horizontal(self):
        """Test field with AdminSplitDateTime widget with layout horizontal."""
        self.assertHTMLEqual(
            self.render('{% bootstrap_field form.test layout="horizontal" %}', context={"form": DateTimeTestForm()}),
            (
                '<div class="django_bootstrap5-req row mb-3">'
                '<label class="col-form-label col-sm-2" for="id_test_0">Test</label>'
                '<div class="col-sm-10">'
                '<p class="datetime">'
                "Date: "
                '<input type="text" name="test_0" class="form-control vDateField" size="10"'
                ' placeholder="Test" required id="id_test_0">'
                "<br>"
                "Time: "
                '<input type="text" name="test_1" class="form-control vTimeField" size="8"'
                ' placeholder="Test" required id="id_test_1">'
                "</p>"
                "</div>"
                "</div>"
            ),
        )

    def test_input_type_admin_split_date_time_floating(self):
        """Test field with AdminSplitDateTime widget with layout floating."""
        self.assertHTMLEqual(
            self.render('{% bootstrap_field form.test layout="floating" %}', context={"form": DateTimeTestForm()}),
            (
                '<div class="django_bootstrap5-req mb-3">'
                '<label class="form-label" for="id_test_0">Test</label>'
                '<p class="datetime">'
                "Date: "
                '<input type="text" name="test_0" class="form-control vDateField" size="10"'
                ' placeholder="Test" required id="id_test_0">'
                "<br>"
                "Time: "
                '<input type="text" name="test_1" class="form-control vTimeField" size="8"'
                ' placeholder="Test" required id="id_test_1">'
                "</p>"
                "</div>"
            ),
        )
