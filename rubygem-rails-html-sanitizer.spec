#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rails-html-sanitizer
Version  : 1.0.2
Release  : 3
URL      : https://rubygems.org/downloads/rails-html-sanitizer-1.0.2.gem
Source0  : https://rubygems.org/downloads/rails-html-sanitizer-1.0.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-activesupport
BuildRequires : rubygem-i18n
BuildRequires : rubygem-loofah
BuildRequires : rubygem-mini_portile
BuildRequires : rubygem-minitest
BuildRequires : rubygem-nokogiri
BuildRequires : rubygem-rails-deprecated_sanitizer
BuildRequires : rubygem-rails-dom-testing
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-thread_safe
BuildRequires : rubygem-tzinfo

%description
# Rails Html Sanitizers
In Rails 4.2 and above this gem will be responsible for sanitizing HTML fragments in Rails
applications, i.e. in the `sanitize`, `sanitize_css`, `strip_tags` and `strip_links` methods.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rails-html-sanitizer-1.0.2
gem spec %{SOURCE0} -l --ruby > rubygem-rails-html-sanitizer.gemspec

%build
gem build rubygem-rails-html-sanitizer.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rails-html-sanitizer-1.0.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/rails-html-sanitizer-1.0.2
ruby -v -I.:lib:test test*/*_test.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/rails-html-sanitizer-1.0.2.gem
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/ActionView/Helpers/SanitizeHelper/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/ActionView/Helpers/SanitizeHelper/ClassMethods/deprecate_option-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/ActionView/Helpers/SanitizeHelper/ClassMethods/sanitized_allowed_attributes%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/ActionView/Helpers/SanitizeHelper/ClassMethods/sanitized_allowed_tags%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/ActionView/Helpers/SanitizeHelper/cdesc-SanitizeHelper.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/ActionView/Helpers/cdesc-Helpers.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/ActionView/cdesc-ActionView.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/FullSanitizer/cdesc-FullSanitizer.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/FullSanitizer/sanitize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/LinkSanitizer/cdesc-LinkSanitizer.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/LinkSanitizer/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/LinkSanitizer/sanitize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/PermitScrubber/allowed_node%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/PermitScrubber/attributes%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/PermitScrubber/attributes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/PermitScrubber/cdesc-PermitScrubber.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/PermitScrubber/keep_node%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/PermitScrubber/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/PermitScrubber/scrub-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/PermitScrubber/scrub_attribute%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/PermitScrubber/scrub_attributes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/PermitScrubber/scrub_css_attribute-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/PermitScrubber/scrub_node-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/PermitScrubber/skip_node%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/PermitScrubber/tags%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/PermitScrubber/tags-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/PermitScrubber/validate%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/Sanitizer/cdesc-Sanitizer.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/Sanitizer/full_sanitizer-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/Sanitizer/link_sanitizer-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/Sanitizer/white_list_sanitizer-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/TargetScrubber/allowed_node%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/TargetScrubber/cdesc-TargetScrubber.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/TargetScrubber/scrub_attribute%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/WhiteListSanitizer/allowed_attributes-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/WhiteListSanitizer/allowed_attributes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/WhiteListSanitizer/allowed_tags-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/WhiteListSanitizer/allowed_tags-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/WhiteListSanitizer/cdesc-WhiteListSanitizer.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/WhiteListSanitizer/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/WhiteListSanitizer/properly_encode-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/WhiteListSanitizer/sanitize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/WhiteListSanitizer/sanitize_css-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/Html/cdesc-Html.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/Rails/cdesc-Rails.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-html-sanitizer-1.0.2/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/rails-html-sanitizer-1.0.2/CHANGELOG.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-html-sanitizer-1.0.2/LICENSE.txt
/usr/lib64/ruby/gems/2.2.0/gems/rails-html-sanitizer-1.0.2/README.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-html-sanitizer-1.0.2/lib/rails-html-sanitizer.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-html-sanitizer-1.0.2/lib/rails/html/sanitizer.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-html-sanitizer-1.0.2/lib/rails/html/sanitizer/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-html-sanitizer-1.0.2/lib/rails/html/scrubbers.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-html-sanitizer-1.0.2/test/sanitizer_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-html-sanitizer-1.0.2/test/scrubbers_test.rb
/usr/lib64/ruby/gems/2.2.0/specifications/rails-html-sanitizer-1.0.2.gemspec
