from django.test import TestCase
from . import forms
# Create your tests here.

class SampleChoiceFormTest(TestCase):
    def test_01(self) -> None:
        """SampleChoiceFormのchoice1を選択しないとエラー"""
        data = {
            'choice1': ''
        }
        form = forms.SampleChoiceForm(data)
        self.assertFalse(form.is_valid())


    def test_02(self) -> None:
        """SampleChoiceFormのchoice1でchoiceに存在する値を選択すると正常"""
        data = {
            'choice1': 'ja'
        }
        form = forms.SampleChoiceForm(data)
        self.assertTrue(form.is_valid())

    def test_03(self) -> None:
        """SampleChoiceFormのchoice1でchoiceに存在しない値を選択するとエラー"""
        data = {
            'choice1': 'fr'
        }
        form = forms.SampleChoiceForm(data)
        self.assertFalse(form.is_valid())

class SampleChoiceAddFormTest(TestCase):
    def test_01(self) -> None:
        """SampleChoiceAddFormのインスタンスのchoicesに設定した値を選択すると正常"""
        data = {
            'choice1': '2'
        }
        form = forms.SampleChoiceAddForm(data)
        form.fields['choice1'].choices = [
            ('0', '0番目'),
            ('1', '1番目'),
            ('2', '2番目'),
            ('3', '3番目'),
            ('4', '4番目'),
        ]
        self.assertTrue(form.is_valid())

    def test_02(self) -> None:
        """SampleChoiceAddFormのインスタンスのchoicesに設定した値以外の値を選択するとエラー"""
        data = {
            'choice1': '5'
        }
        form = forms.SampleChoiceAddForm(data)
        form.fields['choice1'].choices = [
            ('0', '0番目'),
            ('1', '1番目'),
            ('2', '2番目'),
            ('3', '3番目'),
            ('4', '4番目'),
        ]
        self.assertFalse(form.is_valid())