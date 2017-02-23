from models import *
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


class Filter_applicants:

    @classmethod
    def filter_applicants_name(cls):
        name_result = []
        # subquery = Applicant.select()
        if request.form['filter_input_name']:
            for i in request.form['filter_input_name'].split():
                i.lower()
                try:
                    foo = Applicant.select().where((fn.lower(Applicant.first_name) == i) | (fn.lower(Applicant.last_name) == i))#.get()
                    for i in foo:
                        if i not in name_result:
                            name_result.append(i)
                except:
                    continue
            return name_result  # list_applicants(applicants=cls.name_result)
        else:
            return None

    @classmethod
    def filter_applicants_email(cls):
        input = request.form['filter_input_email']
        bar = lambda x: x.email == input
        query = Applicant.select().order_by(Applicant.first_name)
        email_result = filter(bar, query)
        return email_result

    @classmethod
    def filter_applicants_city(cls):
        input = request.form['filter_input_city']
        bar = lambda x: x.applicant_city == input
        query = Applicant.select().order_by(Applicant.first_name)
        city_result = filter(bar, query)
        return city_result


    @classmethod
    def filter_applicants_school(cls):
        input = request.form['filter_input_school']
        bar = lambda x: x.applied_school.city == input
        query = Applicant.select().join(School).order_by(Applicant.first_name)
        city_result = filter(bar, query)
        return city_result


    @classmethod
    def filter_applicants_status(cls):
        input = request.form['filter_input_status']
        bar = lambda x: x.status == input
        query = Applicant.select().order_by(Applicant.first_name)
        status_result = filter(bar, query)
        return status_result




