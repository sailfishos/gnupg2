Name:       gnupg2
Summary:    Utility for secure communication and data storage
Version:    2.0.4
Release:    3
Epoch:      1
Group:      Applications/System
License:    GPLv2+
URL:        git://git.gnupg.org/gnupg.git
Source0:    %{name}-%{version}.tar.bz2
Patch0:     gnupg-2_0_4-curl_easy_setopt_para_error.patch
Patch1:     gnupg_bmc5114_cve_2010_2547.patch
Patch2:     gnupg_sexp_nth_mpi.patch
Patch3:     scripts-Use-POSIX-compatible-arguments-for-find.patch
Patch4:     gnupg2-Don-t-use-deprecated-debug-macros.patch
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  bzip2-devel
BuildRequires:  gettext
BuildRequires:  automake
BuildRequires:  libassuan-devel >= 1.0.4
BuildRequires:  libgpg-error-devel
BuildRequires:  libksba-devel
BuildRequires:  pth-devel
BuildRequires:  zlib-devel


%description
GnuPG is GNU's tool for secure communication and data storage.  It can
be used to encrypt data and to create digital signatures.  It includes
an advanced key management facility and is compliant with the proposed
OpenPGP Internet standard as described in RFC2440 and the S/MIME
standard as described by several RFCs.

GnuPG 2.0 is the stable version of GnuPG integrating support for
OpenPGP and S/MIME.  It does not conflict with an installed 1.x
OpenPGP-only version.

GnuPG 2.0 is a newer version of GnuPG with additional support for
S/MIME.  It has a different design philosophy that splits
functionality up into several modules.  Both versions may be installed
simultaneously without any conflict (gpg is called gpg2 in GnuPG 2).
In fact, the gpg version from GnuPG 1.x is able to make use of the
gpg-agent as included in GnuPG 2 and allows for seamless passphrase
caching.  The advantage of GnupG 1.x is its smaller size and no
dependency on other modules at run and build time.

%package doc
Summary: Documentation package for GnuPG.

%description doc
Documentation package for GnuPG.

%prep
%setup -q -n %{name}-%{version}/%{name}

# gnupg-2_0_4-curl_easy_setopt_para_error.patch
%patch0 -p1
# gnupg_bmc5114_cve_2010_2547.patch
%patch1 -p1
# gnupg_sexp_nth_mpi.patch
%patch2 -p1
# scripts-Use-POSIX-compatible-arguments-for-find.patch
%patch3 -p1
# gnupg2-Don-t-use-deprecated-debug-macros.patch
%patch4 -p1

%build
autoreconf -vfi
%configure --disable-static \
    --disable-doc \
    --without-readline
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install 
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
        AUTHORS ChangeLog NEWS README THANKS TODO

%find_lang gnupg2

%files -f gnupg2.lang
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/gpg2
%{_bindir}/gpgv2
%{_bindir}/gpg-connect-agent
%{_bindir}/gpg-agent
%{_bindir}/gpgconf
%{_bindir}/gpgkey2ssh
%{_bindir}/gpgparsemail
%{_bindir}/gpgsm*
%{_bindir}/kbxutil
%{_bindir}/scdaemon
%{_bindir}/watchgnupg
%{_sbindir}/*
%{_datadir}/gnupg/
%{_libexecdir}/*

%files doc
%{_docdir}/%{name}-%{version}
