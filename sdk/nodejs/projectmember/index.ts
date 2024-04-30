// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { GroupArgs, GroupState } from "./group";
export type Group = import("./group").Group;
export const Group: typeof import("./group").Group = null as any;
utilities.lazyLoad(exports, ["Group"], () => require("./group"));

export { ServiceAccountArgs, ServiceAccountState } from "./serviceAccount";
export type ServiceAccount = import("./serviceAccount").ServiceAccount;
export const ServiceAccount: typeof import("./serviceAccount").ServiceAccount = null as any;
utilities.lazyLoad(exports, ["ServiceAccount"], () => require("./serviceAccount"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "doppler:projectMember/group:Group":
                return new Group(name, <any>undefined, { urn })
            case "doppler:projectMember/serviceAccount:ServiceAccount":
                return new ServiceAccount(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("doppler", "projectMember/group", _module)
pulumi.runtime.registerResourceModule("doppler", "projectMember/serviceAccount", _module)
