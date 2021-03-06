'''
The 'real' module is actually a class, and implements the __getattr__ to
intercept attribute calls to generate (and cache) the individual classes.

Currently, the table_lookup contains a class -> table mapping. This will soon
be augmented with a 'generator' that will derive the table name from the class
being requested, and if there is no table by that name, it will throw an
AttributeError.

Created on Jun 19, 2013

@author: bcrochet
'''
# -*- coding: utf-8 -*-
# pylint: disable=R0903
# pylint: disable=C0103
import sys
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

class Db(object):
    '''
    The actual implementation of the 'module'
    '''
    def __init__(self):
        self.metadata = MetaData()
        self.engine = None
        self.Base = declarative_base()

    def __getattr__(self, name):
        # Lookup actual table name in dict
        if name in self.table_lookup.keys():
            table_name = self.table_lookup[name]
            self.metadata.reflect(bind=self.engine,only=[table_name])
            table = self.metadata.tables[table_name]
            # Now, create the class to represent this thing
            cls = type(name, (self.Base,),
                    dict(__table__=table, __module__=self.__module__))
            setattr(self, name, cls)
            return cls
        else:
            raise AttributeError

    table_lookup = {
        'Account': 'accounts',
        'AdvancedSetting': 'advanced_settings',
        'AssignedServerRole': 'assigned_server_roles',
        'AuditEvent': 'audit_events',
        'Authentication': 'authentications',
        'BinaryBlob': 'binary_blobs',
        'BinaryBlobPart': 'binary_blob_parts',
        'BottleneckEvent': 'bottleneck_events',
        'ChargebackRate': 'chargeback_rates',
        'ChargebackRateDetail': 'chargeback_rate_details',
        'Classification': 'classifications',
        'Compliance': 'compliances',
        'ComplianceDetail': 'compliance_details',
        'Condition': 'conditions',
        'ConditionMiqPolicy': 'conditions_miq_policies',
        'Configuration': 'configurations',
        'CustomAttribute': 'custom_attributes',
        'CustomButton': 'custom_buttons',
        'CustomizationSpec': 'customization_specs',
        'CustomizationTemplate': 'customization_templates',
        'DatabaseBackup': 'database_backups',
        'Dialog': 'dialogs',
        'DialogField': 'dialog_fields',
        'DialogGroup': 'dialog_groups',
        'DialogResource': 'dialog_resources',
        'DialogTab': 'dialog_tabs',
        'Disk': 'disks',
        'DriftState': 'drift_states',
        'EmCluster': 'ems_clusters',
        'EmEvent': 'ems_events',
        'EmFolder': 'ems_folders',
        'EventLog': 'event_logs',
        'ExtManagementSystem': 'ext_management_systems',
        'ExtManagementSystemVdiDesktopPool': 'ext_management_systems_vdi_desktop_pools',
        'FileDepot': 'file_depots',
        'Filesystem': 'filesystems',
        'FirewallRule': 'firewall_rules',
        'GuestApplication': 'guest_applications',
        'GuestDevice': 'guest_devices',
        'Hardware': 'hardwares',
        'Host': 'hosts',
        'HostStorage': 'hosts_storages',
        'IsoDatastore': 'iso_datastores',
        'IsoImage': 'iso_images',
        'Job': 'jobs',
        'Lan': 'lans',
        'LdapDomain': 'ldap_domains',
        'LdapGroup': 'ldap_groups',
        'LdapManagement': 'ldap_managements',
        'LdapRegion': 'ldap_regions',
        'LdapServer': 'ldap_servers',
        'LdapUser': 'ldap_users',
        'LifecycleEvent': 'lifecycle_events',
        'LogFile': 'log_files',
        'Metric': 'metrics',
        'Metric00': 'metrics_00',
        'Metric01': 'metrics_01',
        'Metric02': 'metrics_02',
        'Metric03': 'metrics_03',
        'Metric04': 'metrics_04',
        'Metric05': 'metrics_05',
        'Metric06': 'metrics_06',
        'Metric07': 'metrics_07',
        'Metric08': 'metrics_08',
        'Metric09': 'metrics_09',
        'Metric10': 'metrics_10',
        'Metric11': 'metrics_11',
        'Metric12': 'metrics_12',
        'Metric13': 'metrics_13',
        'Metric14': 'metrics_14',
        'Metric15': 'metrics_15',
        'Metric16': 'metrics_16',
        'Metric17': 'metrics_17',
        'Metric18': 'metrics_18',
        'Metric19': 'metrics_19',
        'Metric20': 'metrics_20',
        'Metric21': 'metrics_21',
        'Metric22': 'metrics_22',
        'Metric23': 'metrics_23',
        'MetricRollup': 'metric_rollups',
        'MetricRollup01': 'metric_rollups_01',
        'MetricRollup02': 'metric_rollups_02',
        'MetricRollup03': 'metric_rollups_03',
        'MetricRollup04': 'metric_rollups_04',
        'MetricRollup05': 'metric_rollups_05',
        'MetricRollup06': 'metric_rollups_06',
        'MetricRollup07': 'metric_rollups_07',
        'MetricRollup08': 'metric_rollups_08',
        'MetricRollup09': 'metric_rollups_09',
        'MetricRollup10': 'metric_rollups_10',
        'MetricRollup11': 'metric_rollups_11',
        'MetricRollup12': 'metric_rollups_12',
        'MiqAction': 'miq_actions',
        'MiqAeClasse': 'miq_ae_classes',
        'MiqAeField': 'miq_ae_fields',
        'MiqAeInstance': 'miq_ae_instances',
        'MiqAeMethod': 'miq_ae_methods',
        'MiqAeNamespace': 'miq_ae_namespaces',
        'MiqAeValue': 'miq_ae_values',
        'MiqAeWorkspace': 'miq_ae_workspaces',
        'MiqAlert': 'miq_alerts',
        'MiqAlertStatuse': 'miq_alert_statuses',
        'MiqApproval': 'miq_approvals',
        'MiqCimAssociation': 'miq_cim_associations',
        'MiqCimDerivedMetric': 'miq_cim_derived_metrics',
        'MiqCimInstance': 'miq_cim_instances',
        'MiqDatabase': 'miq_databases',
        'MiqDialog': 'miq_dialogs',
        'MiqEnterprise': 'miq_enterprises',
        'MiqEvent': 'miq_events',
        'MiqGlobal': 'miq_globals',
        'MiqGroup': 'miq_groups',
        'MiqLicenseContent': 'miq_license_contents',
        'MiqPolicy': 'miq_policies',
        'MiqPolicyContent': 'miq_policy_contents',
        'MiqProductFeature': 'miq_product_features',
        'MiqProxieProductUpdate': 'miq_proxies_product_updates',
        'MiqProxy': 'miq_proxies',
        'MiqQueue': 'miq_queue',
        'MiqRegion': 'miq_regions',
        'MiqReport': 'miq_reports',
        'MiqReportResult': 'miq_report_results',
        'MiqReportResultDetail': 'miq_report_result_details',
        'MiqRequest': 'miq_requests',
        'MiqRequestTask': 'miq_request_tasks',
        'MiqRoleFeature': 'miq_roles_features',
        'MiqSchedule': 'miq_schedules',
        'MiqScsiLun': 'miq_scsi_luns',
        'MiqScsiTarget': 'miq_scsi_targets',
        'MiqSearche': 'miq_searches',
        'MiqServer': 'miq_servers',
        'MiqServerProductUpdate': 'miq_servers_product_updates',
        'MiqSet': 'miq_sets',
        'MiqShortcut': 'miq_shortcuts',
        'MiqStorageMetric': 'miq_storage_metrics',
        'MiqTask': 'miq_tasks',
        'MiqUserRole': 'miq_user_roles',
        'MiqWidget': 'miq_widgets',
        'MiqWidgetContent': 'miq_widget_contents',
        'MiqWidgetShortcut': 'miq_widget_shortcuts',
        'MiqWorker': 'miq_workers',
        'Network': 'networks',
        'OntapAggregateDerivedMetric': 'ontap_aggregate_derived_metrics',
        'OntapAggregateMetricRollup': 'ontap_aggregate_metrics_rollups',
        'OntapDiskDerivedMetric': 'ontap_disk_derived_metrics',
        'OntapDiskMetricRollup': 'ontap_disk_metrics_rollups',
        'OntapLunDerivedMetric': 'ontap_lun_derived_metrics',
        'OntapLunMetricRollup': 'ontap_lun_metrics_rollups',
        'OntapSystemDerivedMetric': 'ontap_system_derived_metrics',
        'OntapSystemMetricRollup': 'ontap_system_metrics_rollups',
        'OntapVolumeDerivedMetric': 'ontap_volume_derived_metrics',
        'OntapVolumeMetricRollup': 'ontap_volume_metrics_rollups',
        'OperatingSystem': 'operating_systems',
        'OProcesse': 'os_processes',
        'Partition': 'partitions',
        'Patche': 'patches',
        'Picture': 'pictures',
        'PolicyEvent': 'policy_events',
        'PolicyEventContent': 'policy_event_contents',
        'ProductUpdate': 'product_updates',
        'ProxyTask': 'proxy_tasks',
        'PxeImage': 'pxe_images',
        'PxeImageType': 'pxe_image_types',
        'PxeMenu': 'pxe_menus',
        'PxeServer': 'pxe_servers',
        'RegistryItem': 'registry_items',
        'Relationship': 'relationships',
        'Repository': 'repositories',
        'Reserve': 'reserves',
        'ResourceAction': 'resource_actions',
        'ResourcePool': 'resource_pools',
        'RsFeed': 'rss_feeds',
        'ScanHistory': 'scan_histories',
        'ScanItem': 'scan_items',
        'SchemaMigration': 'schema_migrations',
        'ServerRole': 'server_roles',
        'Service': 'services',
        'ServiceResource': 'service_resources',
        'ServiceTemplate': 'service_templates',
        'ServiceTemplateCatalog': 'service_template_catalogs',
        'Session': 'sessions',
        'Snapshot': 'snapshots',
        'Storage': 'storages',
        'StorageFile': 'storage_files',
        'StorageManager': 'storage_managers',
        'StorageMetricMetadata': 'storage_metrics_metadata',
        'StorageVmAndTemplate': 'storages_vms_and_templates',
        'Switche': 'switches',
        'SystemService': 'system_services',
        'Tag': 'tags',
        'Tagging': 'taggings',
        'TimeProfile': 'time_profiles',
        'UiTask': 'ui_tasks',
        'User': 'users',
        'VdiController': 'vdi_controllers',
        'VdiDesktop': 'vdi_desktops',
        'VdiDesktopPool': 'vdi_desktop_pools',
        'VdiDesktopPoolVdiUser': 'vdi_desktop_pools_vdi_users',
        'VdiDesktopVdiUser': 'vdi_desktops_vdi_users',
        'VdiEndpointDevice': 'vdi_endpoint_devices',
        'VdiFarm': 'vdi_farms',
        'VdiSession': 'vdi_sessions',
        'VdiUser': 'vdi_users',
        'VimPerformanceOperatingRange': 'vim_performance_operating_ranges',
        'VimPerformanceState': 'vim_performance_states',
        'VimPerformanceTagValue': 'vim_performance_tag_values',
        'Vm': 'vms',
        'VmdbDatabase': 'vmdb_databases',
        'VmdbDatabaseMetric': 'vmdb_database_metrics',
        'VmdbIndex': 'vmdb_indexes',
        'VmdbMetric': 'vmdb_metrics',
        'VmdbTable': 'vmdb_tables',
        'Volume': 'volumes',
        'WindowImage': 'windows_images',
        'Zone': 'zones'
    }

sys.modules[__name__] = Db()