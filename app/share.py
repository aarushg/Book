from flask import Blueprint, Flask, flash, redirect, render_template, request, url_for


share = Blueprint("share", __name__, static_folder="static",
                  template_folder="templates")

@auth.route('/share', methods=['POST'])
@app.route('/share')
    def share():
    print 'I got clicked!'

    return 'Click.'