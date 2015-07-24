#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'DreamCatcher'
__version__ = '1.0.0'

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

import json,urllib2,urllib,gzip,collections


def _parse_json(s):
    ' parse str into JsonDict '

    def _obj_hook(pairs):
        ' convert json object to python object '
        o = JsonDict()
        for k, v in pairs.iteritems():
            o[str(k)] = v
        return o
    return json.loads(s, object_hook=_obj_hook)

class JsonDict(dict):
    ' general json object that allows attributes to be bound to and also behaves like a dict '

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError(r"'JsonDict' object has no attribute '%s'" % attr)

    def __setattr__(self, attr, value):
        self[attr] = value

def _encode_params(**kw):
    '''
    do url-encode parameters

    >>> _encode_params(a=1, b='R&D')
    'a=1&b=R%26D'
    >>> _encode_params(a=u'\u4e2d\u6587', b=['A', 'B', 123])
    'a=%E4%B8%AD%E6%96%87&b=A&b=B&b=123'
    '''
    args = []
    for k, v in kw.iteritems():
        if isinstance(v, basestring):
            qv = v.encode('utf-8') if isinstance(v, unicode) else v
            args.append('%s=%s' % (k, urllib.quote(qv)))
        elif isinstance(v, collections.Iterable):
            for i in v:
                qv = i.encode('utf-8') if isinstance(i, unicode) else str(i)
                args.append('%s=%s' % (k, urllib.quote(qv)))
        else:
            qv = str(v)
            args.append('%s=%s' % (k, urllib.quote(qv)))
    return '&'.join(args)


def _read_body(obj):
    using_gzip = obj.headers.get('Content-Encoding', '')=='gzip'
    body = obj.read()
    if using_gzip:
        gzipper = gzip.GzipFile(fileobj=StringIO(body))
        fcontent = gzipper.read()
        gzipper.close()
        return fcontent
    return body


class EasygoClient(object):
    def __init__(self,openid='ot5aas1gv5RQ1dOFrlqBp4HcvKqM',domain='http://easygo.qq.com'):
        self.openid = openid
        self.domain = domain

    def setOpenid(openid)
        self.openid = openid

    def __getattr__(self,attr):
        return _Callable('%s/%s'%(self.domain,attr),self.openid)

class _Callable(object):
    def __init__(self,client,openid):
        self.client = client
        self.openid = openid
    
    def __getattr__(self,attr):
        def execute(**kw):
            params = 'openid=%s&%s'%(self.openid,_encode_params(**kw))
            http_url = '%s?%s'%(self.client,params) if self.method=='get' else self.client
            http_body = None if self.method == 'get' else params
            req = urllib2.Request(http_url,data=http_body)
            req.add_header('Accept-Encoding', 'gzip')
            try:
                resp = urllib2.urlopen(req)
                body = _read_body(resp)
                r = _parse_json(body)
                return r
            except urllib2.HTTPError, e:
                raise e
        if attr == 'get':
            self.method = 'get'
            return execute
        if attr == 'post':
            self.method = 'post'
            return execute
        return _Callable('%s/%s'%(self.client,attr))
if __name__=='__main__':
    easygoClient = EasygoClient('ot5aas1gv5RQ1dOFrlqBp4HcvKqM')
    data = easygoClient.get_heatmap_data.get(lng0=118.298895,lat0=32.261379,lng1=118.31489499999999,lat1=32.277379)
    print len(data['body']['grid_result'])