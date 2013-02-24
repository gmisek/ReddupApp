# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Claim.issue_id'
        db.delete_column('scru_claim', 'issue_id_id')

        # Deleting field 'Claim.user_id'
        db.delete_column('scru_claim', 'user_id_id')

        # Adding field 'Claim.issue'
        db.add_column('scru_claim', 'issue',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['scru.Issue']),
                      keep_default=False)

        # Adding field 'Claim.user'
        db.add_column('scru_claim', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Issue.cleaner_id'
        db.delete_column('scru_issue', 'cleaner_id_id')

        # Deleting field 'Issue.opener_id'
        db.delete_column('scru_issue', 'opener_id_id')

        # Deleting field 'Issue.location_type_id'
        db.delete_column('scru_issue', 'location_type_id_id')

        # Deleting field 'Issue.closer_id'
        db.delete_column('scru_issue', 'closer_id_id')

        # Deleting field 'Issue.category_id'
        db.delete_column('scru_issue', 'category_id_id')

        # Adding field 'Issue.opener'
        db.add_column('scru_issue', 'opener',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='issue_opener', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Issue.closer'
        db.add_column('scru_issue', 'closer',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='issue_closer', null=True, blank=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Issue.cleaner'
        db.add_column('scru_issue', 'cleaner',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='issue_cleaner', null=True, blank=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Issue.category'
        db.add_column('scru_issue', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['scru.Category']),
                      keep_default=False)

        # Adding field 'Issue.location_type'
        db.add_column('scru_issue', 'location_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['scru.LocationType']),
                      keep_default=False)

        # Deleting field 'Pledge.user_id'
        db.delete_column('scru_pledge', 'user_id_id')

        # Adding field 'Pledge.user'
        db.add_column('scru_pledge', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'IssueUser.issue_id'
        db.delete_column('scru_issueuser', 'issue_id_id')

        # Deleting field 'IssueUser.user_id'
        db.delete_column('scru_issueuser', 'user_id_id')

        # Adding field 'IssueUser.issue'
        db.add_column('scru_issueuser', 'issue',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['scru.Issue']),
                      keep_default=False)

        # Adding field 'IssueUser.user'
        db.add_column('scru_issueuser', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Claim.issue_id'
        db.add_column('scru_claim', 'issue_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['scru.Issue']),
                      keep_default=False)

        # Adding field 'Claim.user_id'
        db.add_column('scru_claim', 'user_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Claim.issue'
        db.delete_column('scru_claim', 'issue_id')

        # Deleting field 'Claim.user'
        db.delete_column('scru_claim', 'user_id')

        # Adding field 'Issue.cleaner_id'
        db.add_column('scru_issue', 'cleaner_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='issue_cleaner', null=True, to=orm['auth.User'], blank=True),
                      keep_default=False)

        # Adding field 'Issue.opener_id'
        db.add_column('scru_issue', 'opener_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='issue_opener', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Issue.location_type_id'
        db.add_column('scru_issue', 'location_type_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['scru.LocationType']),
                      keep_default=False)

        # Adding field 'Issue.closer_id'
        db.add_column('scru_issue', 'closer_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='issue_closer', null=True, to=orm['auth.User'], blank=True),
                      keep_default=False)

        # Adding field 'Issue.category_id'
        db.add_column('scru_issue', 'category_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['scru.Category']),
                      keep_default=False)

        # Deleting field 'Issue.opener'
        db.delete_column('scru_issue', 'opener_id')

        # Deleting field 'Issue.closer'
        db.delete_column('scru_issue', 'closer_id')

        # Deleting field 'Issue.cleaner'
        db.delete_column('scru_issue', 'cleaner_id')

        # Deleting field 'Issue.category'
        db.delete_column('scru_issue', 'category_id')

        # Deleting field 'Issue.location_type'
        db.delete_column('scru_issue', 'location_type_id')

        # Adding field 'Pledge.user_id'
        db.add_column('scru_pledge', 'user_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Pledge.user'
        db.delete_column('scru_pledge', 'user_id')

        # Adding field 'IssueUser.issue_id'
        db.add_column('scru_issueuser', 'issue_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['scru.Issue']),
                      keep_default=False)

        # Adding field 'IssueUser.user_id'
        db.add_column('scru_issueuser', 'user_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'IssueUser.issue'
        db.delete_column('scru_issueuser', 'issue_id')

        # Deleting field 'IssueUser.user'
        db.delete_column('scru_issueuser', 'user_id')


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
        'scru.claim': {
            'Meta': {'object_name': 'Claim'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scru.Issue']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'scru.issue': {
            'Meta': {'object_name': 'Issue'},
            'after_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'before_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scru.Category']"}),
            'cleaner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'issue_cleaner'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"}),
            'closer': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'issue_closer'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"}),
            'date_closed': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_opened': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scru.LocationType']"}),
            'opener': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'issue_opener'", 'to': "orm['auth.User']"}),
            'reported_to_311': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'open'", 'max_length': '100'})
        },
        'scru.issueuser': {
            'Meta': {'object_name': 'IssueUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scru.Issue']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['scru']