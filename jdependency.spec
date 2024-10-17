%{?_javapackages_macros:%_javapackages_macros}
Name:           jdependency
Version:        0.7
Release:        9.0%{?dist}
Summary:        This project provides an API to analyse class dependencies
License:        ASL 2.0
URL:            https://github.com/tcurdt/%{name}
BuildArch:      noarch

Source0:        http://github.com/tcurdt/%{name}/archive/%{name}-%{version}.tar.gz
# Upstream uses different version of objectweb-asm than Fedora has.
Patch0:         %{name}-asm.patch

BuildRequires:  maven-local
BuildRequires:  objectweb-asm
BuildRequires:  apache-commons-io

%description
%{name} is small library that helps you analyze class level
dependencies, clashes and missing classes.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0
%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7-8
- Update to current packaging guidelines
- Fix test failures

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7-7
- Remove unneeded BR: maven-idea-plugin

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.7-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.7-3
- Fix date ordering in changelog
- Guidelines fixes

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 13 2011 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7-1
- Update to 0.7
- Fix BR to not require maven2
- Fix BR for new package name
- Adjust spec to new guidelines

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6-3
- Add license to javadoc subpackage
- Change jakarta-commons-io for apache-commons-io
- Add BR to maven

* Thu Oct 14 2010 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6-2
- Rename from vafer-jdependency to jdependency alone

* Thu Oct 14 2010 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6-1
- Initial package
