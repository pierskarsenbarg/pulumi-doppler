// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package doppler

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-doppler/sdk/go/doppler/internal"
)

type Config struct {
	pulumi.CustomResourceState

	// The name of the Doppler environment where the config is located
	Environment pulumi.StringOutput `pulumi:"environment"`
	// The name of the Doppler config
	Name pulumi.StringOutput `pulumi:"name"`
	// The name of the Doppler project where the config is located
	Project pulumi.StringOutput `pulumi:"project"`
}

// NewConfig registers a new resource with the given unique name, arguments, and options.
func NewConfig(ctx *pulumi.Context,
	name string, args *ConfigArgs, opts ...pulumi.ResourceOption) (*Config, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Environment == nil {
		return nil, errors.New("invalid value for required argument 'Environment'")
	}
	if args.Project == nil {
		return nil, errors.New("invalid value for required argument 'Project'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Config
	err := ctx.RegisterResource("doppler:index/config:Config", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConfig gets an existing Config resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConfig(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConfigState, opts ...pulumi.ResourceOption) (*Config, error) {
	var resource Config
	err := ctx.ReadResource("doppler:index/config:Config", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Config resources.
type configState struct {
	// The name of the Doppler environment where the config is located
	Environment *string `pulumi:"environment"`
	// The name of the Doppler config
	Name *string `pulumi:"name"`
	// The name of the Doppler project where the config is located
	Project *string `pulumi:"project"`
}

type ConfigState struct {
	// The name of the Doppler environment where the config is located
	Environment pulumi.StringPtrInput
	// The name of the Doppler config
	Name pulumi.StringPtrInput
	// The name of the Doppler project where the config is located
	Project pulumi.StringPtrInput
}

func (ConfigState) ElementType() reflect.Type {
	return reflect.TypeOf((*configState)(nil)).Elem()
}

type configArgs struct {
	// The name of the Doppler environment where the config is located
	Environment string `pulumi:"environment"`
	// The name of the Doppler config
	Name *string `pulumi:"name"`
	// The name of the Doppler project where the config is located
	Project string `pulumi:"project"`
}

// The set of arguments for constructing a Config resource.
type ConfigArgs struct {
	// The name of the Doppler environment where the config is located
	Environment pulumi.StringInput
	// The name of the Doppler config
	Name pulumi.StringPtrInput
	// The name of the Doppler project where the config is located
	Project pulumi.StringInput
}

func (ConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*configArgs)(nil)).Elem()
}

type ConfigInput interface {
	pulumi.Input

	ToConfigOutput() ConfigOutput
	ToConfigOutputWithContext(ctx context.Context) ConfigOutput
}

func (*Config) ElementType() reflect.Type {
	return reflect.TypeOf((**Config)(nil)).Elem()
}

func (i *Config) ToConfigOutput() ConfigOutput {
	return i.ToConfigOutputWithContext(context.Background())
}

func (i *Config) ToConfigOutputWithContext(ctx context.Context) ConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigOutput)
}

// ConfigArrayInput is an input type that accepts ConfigArray and ConfigArrayOutput values.
// You can construct a concrete instance of `ConfigArrayInput` via:
//
//	ConfigArray{ ConfigArgs{...} }
type ConfigArrayInput interface {
	pulumi.Input

	ToConfigArrayOutput() ConfigArrayOutput
	ToConfigArrayOutputWithContext(context.Context) ConfigArrayOutput
}

type ConfigArray []ConfigInput

func (ConfigArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Config)(nil)).Elem()
}

func (i ConfigArray) ToConfigArrayOutput() ConfigArrayOutput {
	return i.ToConfigArrayOutputWithContext(context.Background())
}

func (i ConfigArray) ToConfigArrayOutputWithContext(ctx context.Context) ConfigArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigArrayOutput)
}

// ConfigMapInput is an input type that accepts ConfigMap and ConfigMapOutput values.
// You can construct a concrete instance of `ConfigMapInput` via:
//
//	ConfigMap{ "key": ConfigArgs{...} }
type ConfigMapInput interface {
	pulumi.Input

	ToConfigMapOutput() ConfigMapOutput
	ToConfigMapOutputWithContext(context.Context) ConfigMapOutput
}

type ConfigMap map[string]ConfigInput

func (ConfigMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Config)(nil)).Elem()
}

func (i ConfigMap) ToConfigMapOutput() ConfigMapOutput {
	return i.ToConfigMapOutputWithContext(context.Background())
}

func (i ConfigMap) ToConfigMapOutputWithContext(ctx context.Context) ConfigMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigMapOutput)
}

type ConfigOutput struct{ *pulumi.OutputState }

func (ConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Config)(nil)).Elem()
}

func (o ConfigOutput) ToConfigOutput() ConfigOutput {
	return o
}

func (o ConfigOutput) ToConfigOutputWithContext(ctx context.Context) ConfigOutput {
	return o
}

// The name of the Doppler environment where the config is located
func (o ConfigOutput) Environment() pulumi.StringOutput {
	return o.ApplyT(func(v *Config) pulumi.StringOutput { return v.Environment }).(pulumi.StringOutput)
}

// The name of the Doppler config
func (o ConfigOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Config) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The name of the Doppler project where the config is located
func (o ConfigOutput) Project() pulumi.StringOutput {
	return o.ApplyT(func(v *Config) pulumi.StringOutput { return v.Project }).(pulumi.StringOutput)
}

type ConfigArrayOutput struct{ *pulumi.OutputState }

func (ConfigArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Config)(nil)).Elem()
}

func (o ConfigArrayOutput) ToConfigArrayOutput() ConfigArrayOutput {
	return o
}

func (o ConfigArrayOutput) ToConfigArrayOutputWithContext(ctx context.Context) ConfigArrayOutput {
	return o
}

func (o ConfigArrayOutput) Index(i pulumi.IntInput) ConfigOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Config {
		return vs[0].([]*Config)[vs[1].(int)]
	}).(ConfigOutput)
}

type ConfigMapOutput struct{ *pulumi.OutputState }

func (ConfigMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Config)(nil)).Elem()
}

func (o ConfigMapOutput) ToConfigMapOutput() ConfigMapOutput {
	return o
}

func (o ConfigMapOutput) ToConfigMapOutputWithContext(ctx context.Context) ConfigMapOutput {
	return o
}

func (o ConfigMapOutput) MapIndex(k pulumi.StringInput) ConfigOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Config {
		return vs[0].(map[string]*Config)[vs[1].(string)]
	}).(ConfigOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ConfigInput)(nil)).Elem(), &Config{})
	pulumi.RegisterInputType(reflect.TypeOf((*ConfigArrayInput)(nil)).Elem(), ConfigArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ConfigMapInput)(nil)).Elem(), ConfigMap{})
	pulumi.RegisterOutputType(ConfigOutput{})
	pulumi.RegisterOutputType(ConfigArrayOutput{})
	pulumi.RegisterOutputType(ConfigMapOutput{})
}
