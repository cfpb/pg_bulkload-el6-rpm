%global _version 3.1.7


Name:           pg_bulkload
Version:        %{_version}
Release:        1%{?dist}
Summary: 	High speed data load utility for PostgreSQL

Group:          Applications/Databases
License:        pg_bulkload is released under the PostgreSQL License, a liberal Open Source license, similar to the BSD or MIT licenses
URL:		http://pgfoundry.org/projects/pgbulkload/
Source:		http://pgfoundry.org/frs/download.php/3814/master.tar.gz

Obsoletes:      pg_bulkload <= 3.1.6
Provides:       pg_bulkload = 3.1.7


%description
pg_bulkload provides high-speed data loading capability to PostgreSQL users.

When we load huge amount of data to a database, it is common situation that data set to be loaded is valid and consistent. 
For example, dedicated tools are used to prepare such data, providing data validation in advance. 
In such cases, we'd like to bypass any overheads within database system to load data as quickly as possible. 
pg_bulkload is developed to help such situations. Therefore, it is not pg_bulkload's goal to provide detailed data validation. 
Rather, pg_bulkload asumes that loaded data set is validated by separate means. If you're not in such situation, you should use COPY command in PostgreSQL.


###############################################################################################################################################################
# Build requirements

BuildRoot: %(mktemp -ud %{_tmppath}/build/%{name}-%{version}-%{release}-XXXXXX)


###############################################################################################################################################################
#PREP and SETUP
# The prep directive removes existing build directory and extracts source code so we have a fresh code base .....-n flag where present, defines the name of the directory

%prep
%setup -n %{name}-%{version}
###%setup -n pg_bulkload-master


###############################################################################################################################################################
%build

make


%make_install 




###############################################################################################################################################################
%files
#/usr/lib/debug/
#/usr/pgsql-9.4/


/usr/pgsql-9.4/bin/pg_bulkload
/usr/pgsql-9.4/bin/postgresql
/usr/pgsql-9.4/lib/pg_bulkload.so
/usr/pgsql-9.4/lib/pg_timestamp.so
/usr/pgsql-9.4/share/contrib/pg_timestamp.sql
/usr/pgsql-9.4/share/contrib/uninstall_pg_timestamp.sql
/usr/pgsql-9.4/share/extension/pg_bulkload--1.0.sql
/usr/pgsql-9.4/share/extension/pg_bulkload--unpackaged--1.0.sql
/usr/pgsql-9.4/share/extension/pg_bulkload.control
/usr/pgsql-9.4/share/extension/pg_bulkload.sql
/usr/pgsql-9.4/share/extension/uninstall_pg_bulkload.sql
