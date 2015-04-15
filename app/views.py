from app import app
from flask import request, render_template, redirect, url_for
from models import Dictionary, Blogger

clc = Dictionary

class_map = {
        'dictionary': Dictionary,
        'blogger': Blogger,
    }


@app.route('/')
def show_all():
    return redirect(url_for('show_coll', type='dictionary'))


@app.route('/view/')
def show_coll():
    print request.args
    str_clc = request.args.get('type', 'dictionary')
    print str_clc
    clc = class_map.get(str_clc)
    docs = clc.objects
    return render_template('list.html', docs=docs, str_clc=str_clc)


@app.route('/doc/<doc_id>/', methods=["GET", "POST"])
def show_doc(doc_id):
    str_clc = request.args.get('str_clc', 'dictionary')
    print str_clc
    clc = class_map.get(str_clc)
    doc = clc.objects.get(id=doc_id)
    fields = clc._fields
    print doc
    if request.method == 'GET':
        d = {}
        for field in fields:
            print field
            if field != 'id' and field != 'addtime':
                d[doc[field]] = field
        return render_template('doc.html', doc=doc, d=d, str_clc=str_clc)
    if request.method == 'POST':
        for field in doc:
            if field != 'id' and field != 'addtime':
                print "qui"
                print request.form[field]
                doc.field = request.form[field]
        doc.save()
        return redirect(url_for('show_coll', type=str_clc))


@app.route('/new/', methods=["GET", "POST"])
def new_doc():
    str_clc = request.args.get('str_clc', 'dictionary')
    print str_clc
    clc = class_map.get(str_clc)
    fields = clc._fields
    d = {}
    if request.method == 'POST':
        doc = clc()
        for field in fields:
            if field != 'id' and field != 'addtime':
                d[request.form[field]] = field
        print d
        for k, v in d.items():
            doc[d[k]] = k
        doc.save()
        return redirect(url_for('show_coll', type=str_clc))
    return render_template('new.html', fields=fields, str_clc=str_clc)


@app.route('/del/<doc_id>/<str_clc>/', methods=["DELETE"])
def del_doc(doc_id, str_clc):
    if request.method == 'DELETE':
        print str_clc
        clc = class_map.get(str_clc)
        doc = clc.objects.get(id=doc_id)
        doc.delete()
        return redirect(url_for('show_coll', type=str_clc))
