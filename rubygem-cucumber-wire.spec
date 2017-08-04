# Generated from cucumber-wire-0.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name cucumber-wire

Name: rubygem-%{gem_name}
Version: 0.0.1
Release: 2%{?dist}
Summary: cucumber-wire-0.0.1
Group: Development/Languages
License: MIT
URL: http://cucumber.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.3
# the following BuildRequires are development dependencies
# BuildRequires: rubygem(cucumber) >= 2.1.0
# BuildRequires: rubygem(cucumber) < 2.2
# BuildRequires: rubygem(rspec) >= 3
# BuildRequires: rubygem(rspec) < 4
# BuildRequires: rubygem(aruba)
# BuildRequires: rubygem(aruba) < 1
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Wire protocol for Cucumber.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_instdir}/.rspec
%exclude %{gem_instdir}/.travis.yml
%{gem_instdir}/features
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/cucumber-wire.gemspec
%{gem_instdir}/spec

%changelog
* Thu Sep 22 2016 Rich Megginson <rmeggins@redhat.com> - 0.0.1-2
- bump rev to rebuild for rhlog-buildrequires

* Thu Sep 22 2016 Rich Megginson <rmeggins@redhat.com> - 0.0.1-1
- Initial package
