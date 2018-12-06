# https://gopkg.in/asn1-ber.v1
%global goipath gopkg.in/asn1-ber.v1
%global tag     v1.3

Version:        1.3

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        ASN1 BER Encoding / Decoding Library for Go
License:        MIT

URL:            https://github.com/go-asn1-ber/asn1-ber
Source0:        %{url}/archive/%{tag}/asn1-ber-v1-%{version}.tar.gz

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%autosetup -n asn1-ber-%{version} -p1


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3-1
- Update to version 1.3.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1.2-2
- Use autosetup instead of gosetup.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.2-1
- Initial package for fedora.

