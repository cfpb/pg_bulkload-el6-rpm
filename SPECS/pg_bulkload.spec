%global _version 3.1.7


Name:           pg_bulkload%{suffix}
Version:        %{_version}
Release:        1%{?dist}
Summary: 	High speed data load utility for PostgreSQL

Group:          Applications/Databases
License:        pg_bulkload is released under the PostgreSQL License, a liberal Open Source license, similar to the BSD or MIT licenses
URL:		http://pgfoundry.org/projects/pgbulkload/
Source:		http://pgfoundry.org/frs/download.php/3814/master.tar.gz

Obsoletes:      pg_bulkload%{suffix} <= 3.1.6
Provides:       pg_bulkload%{suffix} => 3.1.7


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

#make

###############################################################################################################################################################
%install
mkdir -p %{buildroot}/etc/profile.d
echo "export PATH=$PATH:%{pg_dir}/bin/" >> %{buildroot}/etc/profile.d/pg_bulkload.sh
echo "export USE_PGXS=1" >> %{buildroot}/etc/profile.d/pg_bulkload.sh
source %{buildroot}/etc/profile.d/pg_bulkload.sh

###%make_install

###############################################################################################################################################################
%clean
# Sanity check before removal of old buildroot files
[ -d "%{buildroot}" -a "%{buildroot}" != "/" ] && rm -rf %{buildroot}
###############################################################################################################################################################
%files
/etc/profile.d/pg_bulkload.sh
