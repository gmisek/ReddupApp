# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Issue'
        db.create_table('scru_issue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('before_img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('after_img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('date_opened', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('date_closed', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('opener_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='issue_opener', to=orm['auth.User'])),
            ('closer_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='issue_closer', to=orm['auth.User'])),
            ('cleaner_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='issue_cleaner', to=orm['auth.User'])),
            ('category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scru.Category'])),
            ('reported_to_311', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('location_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scru.LocationType'])),
        ))
        db.send_create_signal('scru', ['Issue'])

        # Adding model 'LocationType'
        db.create_table('scru_locationtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('appkey', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('scru', ['LocationType'])

        # Adding model 'Category'
        db.create_table('scru_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('appkey', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('scru', ['Category'])

        # Adding model 'IssueUser'
        db.create_table('scru_issueuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issue_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scru.Issue'])),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
        ))
        db.send_create_signal('scru', ['IssueUser'])

        # Adding model 'Pledge'
        db.create_table('scru_pledge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('radius', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, null=True, blank=True)),
        ))
        db.send_create_signal('scru', ['Pledge'])


    def backwards(self, orm):
        # Deleting model 'Issue'
        db.delete_table('scru_issue')

        # Deleting model 'LocationType'
        db.delete_table('scru_locationtype')

        # Deleting model 'Category'
        db.delete_table('scru_category')

        # Deleting model 'IssueUser'
        db.delete_table('scru_issueuser')

        # Deleting model 'Pledge'
        db.delete_table('scru_pledge')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'scru.category': {
            'Meta': {'object_name': 'Category'},
            'appkey': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'scru.issue': {
            'Meta': {'object_name': 'Issue'},
            'after_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'before_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'category_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scru.Category']"}),
            'cleaner_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'issue_cleaner'", 'to': "orm['auth.User']"}),
            'closer_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'issue_closer'", 'to': "orm['auth.User']"}),
            'date_closed': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_opened': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_type_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scru.LocationType']"}),
            'opener_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'issue_opener'", 'to': "orm['auth.User']"}),
            'reported_to_311': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'scru.issueuser': {
            'Meta': {'object_name': 'IssueUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scru.Issue']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'scru.locationtype': {
            'Meta': {'object_name': 'LocationType'},
            'appkey': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'scru.pledge': {
            'Meta': {'object_name': 'Pledge'},
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'radius': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['scru']